from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_classes():
    response = client.get("/classes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "name" in response.json()[0]

def test_book_class():
    # Get classes to book one
    classes = client.get("/classes").json()
    assert len(classes) > 0
    class_id = classes[0]["id"]

    # Book class
    payload = {
        "class_id": class_id,
        "client_name": "Elumalai",
        "client_email": "elumalaiesk7887@gmail.com"
    }
    res = client.post("/book", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["client_email"] == payload["client_email"]

def test_duplicate_email_blocked():
    classes = client.get("/classes").json()
    class_id = classes[0]["id"]

    # Same email again
    payload = {
        "class_id": class_id,
        "client_name": "Elumalai",
        "client_email": "elumalaiesk7887@gmail.com"
    }
    res = client.post("/book", json=payload)
    assert res.status_code == 400
    assert res.json()["detail"] == "You have already booked this class with this email"

def test_get_bookings():
    email = "elumalaiesk7887@gmail.com"
    res = client.get(f"/bookings?email={email}")
    assert res.status_code == 200
    bookings = res.json()
    assert all(b["client_email"] == email for b in bookings)