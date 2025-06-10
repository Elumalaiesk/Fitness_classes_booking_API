## Setup & Run Instructions

1. Clone the repository

   ```bash
   git clone https://github.com/your-username/fitness-booking-api.git
   cd fitness-booking-api
   ```

2. Create & activate virtual environment

   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install required packages

   ```bash
   pip install -r requirements.txt
   ```

4. Run the API

   ```bash
   uvicorn main:app --reload
   ```

5. View & test APIs using Swagger UI
   Open in browser: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

6. Run test cases using Pytest

   ```bash
   pytest test_main.py
   ```
