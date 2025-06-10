🧪 Fitness Booking API
A simple backend API for a fictional fitness studio that allows clients to:

View upcoming classes

Book a slot in a class

View their bookings

Built with FastAPI and SQLite.

🚀 Setup & Run Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/fitness-booking-api.git
cd fitness-booking-api
2. Create and activate a virtual environment
bash
Copy
Edit
python -m venv fitness_env
fitness_env\Scripts\activate  # On Windows
# OR
source fitness_env/bin/activate  # On Mac/Linux
3. Install required packages
bash
Copy
Edit
pip install -r requirements.txt
4. Run the FastAPI server
bash
Copy
Edit
uvicorn main:app --reload
5. Access API docs in your browser
Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

🧪 Running Tests
bash
Copy
Edit
pytest test_main.py
📦 API Endpoints
📘 GET /classes
Returns a list of all upcoming fitness classes.

Sample Response:

json
Copy
Edit
[
  {
    "id": 1,
    "name": "Yoga",
    "datetime": "2025-06-10T06:00:00+00:00",
    "instructor": "Ragavan",
    "available_slots": 10
  }
]
📝 POST /book
Books a slot in a class.

Sample Request:

json
Copy
Edit
{
  "class_id": 1,
  "client_name": "Elumalai Saravanan",
  "client_email": "elumalaiesk7887@gmail.com"
}
📋 GET /bookings?email=your_email@example.com
Returns all bookings for a specific email.

Sample Response:

json
Copy
Edit
[
  {
    "class_id": 1,
    "class_name": "Yoga",
    "class_time": "2025-06-10T06:00:00+00:00",
    "client_name": "Elumalai Saravanan",
    "client_email": "elumalaiesk7887@gmail.com"
  }
]
🌐 Timezone Handling
All class times are created in IST (Asia/Kolkata).

Internally stored in UTC to avoid ambiguity.

Clients are expected to convert the time based on their local timezone when displaying.

🌱 Seed Data
Automatically seeded on first run:

Yoga – Tomorrow

Zumba – Day after tomorrow

HIIT – In 3 days

Each class includes name, datetime, instructor, and available slots.

⚠️ Validations & Error Handling
❌ Duplicate bookings for the same class and email are blocked

❌ Bookings within 1 hour of another class are rejected

❌ Booking a full class is not allowed

❌ Missing or invalid inputs return 400 errors

