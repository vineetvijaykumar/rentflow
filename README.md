# RentFlow

A flexible rent payment scheduling system that helps users manage their rent payments based on their income and risk profile.

## Features

- Flexible payment scheduling
- Risk assessment
- Income-based installment planning
- Payment date optimization

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/vineetvijaykumar/rentflow.git
cd rentflow
```

2. Set up virtual environment:
```bash 
python -m venv venv 
source venv/bin/activate
```

3. Install dependencies:
```bash 
pip install -r requirements.txt
```
4. Run the application:
```bash
uvicorn app.main:app --reload
```
Visit http://localhost:8000/docs for interactive API documentation.

Build and run with Docker Compose:
```bash 
docker-compose up --build
```

Access the application at http://localhost:8000/

Calculate Payment Plan
Create a flexible payment schedule based on income and rent amount.
Endpoint: POST /calculate-payment-plan
Request Body:
```json
{
  "monthly_income": 5000,
  "total_rent": 2000
}
```

Response:
```json
{
    "payment_schedule": {
        "total_rent": 2000,
        "num_installments": 4,
        "installments": [
            {
                "installment_number": 1,
                "amount": 525.00,
                "suggested_date": "2024-12-01"
            },
            {
                "installment_number": 2,
                "amount": 475.00,
                "suggested_date": "2024-12-08"
            }
            // ... additional installments
        ]
    },
    "risk_assessment": {
        "rent_to_income_ratio": 40.0,
        "risk_score": 0.5,
        "risk_category": "MEDIUM_RISK"
    }
}
```

Testing 
Run tests with pytest:
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/
```

Project Structure
```rentflow/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── services/
│       ├── payment_scheduler.py
│       └── risk_assessment.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_payment_scheduler.py
│   └── test_risk_assessment.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

Implementation Details
Risk Assessment

Low Risk: Rent < 30% of income
Medium Risk: Rent 30-50% of income
High Risk: Rent > 50% of income

Payment Scheduling

Minimum 2 installments
Maximum 5 installments
Installment count based on income level
Even distribution across the month

🔒 Security

Input validation using Pydantic models
Error handling for edge cases
Secure payment scheduling logic

🚧 Future Improvements

Add authentication and authorization
Implement persistent storage
Add payment gateway integration
Enhanced risk assessment algorithms
User notification system
Payment history tracking