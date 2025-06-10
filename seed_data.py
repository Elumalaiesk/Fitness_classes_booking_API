from datetime import datetime, timedelta
import pytz
from sqlalchemy.orm import Session
from models import FitnessClass

def seed_classes(db: Session):
    db.query(FitnessClass).delete() 
    db.commit()

    ist = pytz.timezone("Asia/Kolkata")
    now_ist = ist.localize(datetime.now())  # Localize to IST

    classes = [
        {
            "name": "Yoga",
            "time": now_ist + timedelta(days=1),
            "instructor": "Ragavan",
            "slots": 10
        },
        {
            "name": "Zumba",
            "time": now_ist + timedelta(days=2),
            "instructor": "Hrithvik",
            "slots": 8
        },
        {
            "name": "HIIT",
            "time": now_ist + timedelta(days=3),
            "instructor": "Elumalai",
            "slots": 5
        }
    ]

    fitness_classes = [
        FitnessClass(
            name=cls["name"],
            datetime=cls["time"].astimezone(pytz.utc),  # Convert to UTC
            instructor=cls["instructor"],
            available_slots=cls["slots"]
        )
        for cls in classes
    ]

    db.add_all(fitness_classes)
    db.commit()
