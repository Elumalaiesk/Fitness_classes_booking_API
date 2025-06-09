from datetime import datetime, timedelta
import pytz
from sqlalchemy.orm import Session
from models import FitnessClass

def seed_classes(db: Session):
    db.query(FitnessClass).delete()  # 🚨 DANGER: This deletes all existing classes
    db.commit()

    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist)
    classes = [
        FitnessClass(name="Yoga", datetime=now + timedelta(days=1), instructor="Ragavan", available_slots=10),
        FitnessClass(name="Zumba", datetime=now + timedelta(days=2), instructor="Hrithvik", available_slots=8),
        FitnessClass(name="HIIT", datetime=now + timedelta(days=3), instructor="Elumalai", available_slots=5)
    ]
    db.add_all(classes)
    db.commit()