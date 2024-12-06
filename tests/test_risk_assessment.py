# tests/test_risk_assessment.py
import pytest
from app.services.risk_assessment import RiskAssessment


def test_calculate_risk_score():
    risk_assessor = RiskAssessment()

    # Test low-income scenario
    low_income_risk = risk_assessor.calculate_risk_score(
        monthly_income=2000,
        total_rent=1200
    )
    assert low_income_risk['risk_category'] == 'HIGH_RISK'

    # Test medium-income scenario
    medium_income_risk = risk_assessor.calculate_risk_score(
        monthly_income=5000,
        total_rent=1500
    )
    assert medium_income_risk['risk_category'] == 'MEDIUM_RISK'

    # Test high-income scenario
    high_income_risk = risk_assessor.calculate_risk_score(
        monthly_income=8000,
        total_rent=1500
    )
    assert high_income_risk['risk_category'] == 'LOW_RISK'


def test_risk_score_calculation():
    risk_assessor = RiskAssessment()

    risk = risk_assessor.calculate_risk_score(
        monthly_income=5000,
        total_rent=2000
    )

    assert 'rent_to_income_ratio' in risk
    assert 'risk_score' in risk
    assert 'risk_category' in risk