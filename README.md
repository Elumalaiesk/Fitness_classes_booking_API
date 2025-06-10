## Setup & Run Instructions

1. Clone the repository

   ```bash
   git clone https://github.com/your-username/fitness-booking-api.git
   cd fitness-booking-api
   ```

2. Activate virtual environment

   ```bash
   fitness_env\Scripts\activate
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
   Open in browser: [http://127.0.0.1:8000/docs]

6. Run test cases using Pytest

   ```bash
   pytest test_main.py
   ```
