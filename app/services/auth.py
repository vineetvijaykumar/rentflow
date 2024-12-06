# tests/test_main.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_calculate_payment_plan():
    # Test successful payment plan calculation
    response = client.post(
        "/calculate-payment-plan",
        json={
            "monthly_income": 5000,
            "total_rent": 2000
        }
    )

    assert response.status_code == 200

    data = response.json()

    # Verify payment schedule
    assert 'payment_schedule' in data
    assert 'risk_assessment' in data

    payment_schedule = data['payment_schedule']
    assert payment_schedule['total_rent'] == 2000
    assert len(payment_schedule['installments']) > 0

    # Verify risk assessment
    risk_assessment = data['risk_assessment']
    assert 'risk_category' in risk_assessment