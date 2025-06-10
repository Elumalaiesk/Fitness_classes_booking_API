from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from schemas import ClassResponse, BookingRequest, BookingResponse

import pytz
from datetime import timezone

from database import SessionLocal, engine, Base
from models import FitnessClass, Booking
from schemas import ClassResponse, BookingRequest, BookingResponse
from seed_data import seed_classes

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency to get DB session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Seed data on app startup
@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    if not db.query(FitnessClass).first():
        seed_classes(db)
    db.close()

@app.get("/classes", response_model=List[ClassResponse])
def get_classes(db: Session = Depends(get_db)):
    classes = db.query(FitnessClass).all()
    return classes 
@app.post("/book", response_model=BookingResponse)
def book_class(booking: BookingRequest, db: Session = Depends(get_db)):
    selected_class = db.query(FitnessClass).filter(FitnessClass.id == booking.class_id).first()

    if not selected_class:
        raise HTTPException(status_code=404, detail="Class not found")

    if selected_class.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")

    # Check duplicate booking for the same class and email
    duplicate = db.query(Booking).filter(
        Booking.client_email == booking.client_email,
        Booking.class_id == booking.class_id
    ).first()
    if duplicate:
        raise HTTPException(status_code=400, detail="You have already booked this class with this email")

    # Check booking time conflicts (within 1 hour)
    user_bookings = db.query(Booking).filter(Booking.client_email == booking.client_email).all()
    for b in user_bookings:
        booked_class = db.query(FitnessClass).filter(FitnessClass.id == b.class_id).first()
        if booked_class:
            booked_time_utc = booked_class.datetime.astimezone(timezone.utc)
            selected_time_utc = selected_class.datetime.astimezone(timezone.utc)
            time_diff = abs((selected_time_utc - booked_time_utc).total_seconds())
            if time_diff < 3600:
                raise HTTPException(
                    status_code=400,
                    detail=f"You have another booking ({booked_class.name}) within 1 hour of this class."
                )

    # Book the class
    selected_class.available_slots -= 1
    db.add(selected_class)  # To update slots count

    new_booking = Booking(
        class_id=booking.class_id,
        client_name=booking.client_name,
        client_email=booking.client_email
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)

    return BookingResponse(
        id=new_booking.id,
        class_id=new_booking.class_id,
        class_name=selected_class.name,       
        class_time=selected_class.datetime,   
        client_name=new_booking.client_name,
        client_email=new_booking.client_email
    )

@app.get("/bookings", response_model=List[BookingResponse])
def get_bookings(email: str = Query(...), db: Session = Depends(get_db)):
    user_bookings = db.query(Booking).filter(Booking.client_email == email).all()

    responses = []
    for b in user_bookings:
        booked_class = db.query(FitnessClass).filter(FitnessClass.id == b.class_id).first()
        if booked_class:
            responses.append(BookingResponse(
                class_id=b.class_id,
                class_name=booked_class.name,
                class_time=booked_class.datetime,
                client_name=b.client_name,
                client_email=b.client_email
            ))

    return responses

# @app.get("/all-bookings", response_model=List[BookingResponse])
# def get_all_bookings(db: Session = Depends(get_db)):
#     bookings = db.query(Booking).all()
#     return bookings