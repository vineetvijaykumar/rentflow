# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.services.payment_scheduler import PaymentScheduler
from app.services.risk_assessment import RiskAssessment

app = FastAPI(title="RentFlow")


class PaymentRequest(BaseModel):
    monthly_income: float
    total_rent: float


class PaymentResponse(BaseModel):
    payment_schedule: dict
    risk_assessment: dict

@app.get("/")
async def root():
    return {
        "message": "Welcome to RentFlow API",
        "version": "1.0.0",
        "endpoints": {
            "calculate_payment_plan": "/calculate-payment-plan"
        },
        "documentation": "/docs"
    }


@app.post("/calculate-payment-plan")
def calculate_payment_plan(request: PaymentRequest) -> PaymentResponse:
    try:
        # Initialize services
        scheduler = PaymentScheduler()
        risk_assessor = RiskAssessment()

        # Generate payment schedule
        payment_schedule = scheduler.create_flexible_schedule(
            request.total_rent,
            request.monthly_income
        )

        # Assess risk
        risk_assessment = risk_assessor.calculate_risk_score(
            request.monthly_income,
            request.total_rent
        )

        return PaymentResponse(
            payment_schedule=payment_schedule,
            risk_assessment=risk_assessment
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))