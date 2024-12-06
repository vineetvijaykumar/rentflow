# app/services/risk_assessment.py
class RiskAssessment:
    def calculate_risk_score(
            self,
            monthly_income: float,
            total_rent: float
    ) -> dict[str, float]:
        """
        Calculate risk score based on income and rent

        Args:
            monthly_income (float): User's monthly income
            total_rent (float): Total monthly rent

        Returns:
            Risk assessment details
        """
        # Rent-to-Income Ratio
        rent_ratio = (total_rent / monthly_income) * 100

        # Base risk calculation
        if rent_ratio >= 50:
            risk_score = 0.8  # High Risk
        elif rent_ratio >= 30:
            risk_score = 0.5  # Medium Risk
        else:
            risk_score = 0.2  # Low Risk

        # Additional risk factors
        risk_factors = {
            "rent_to_income_ratio": rent_ratio,
            "risk_score": risk_score,
            "risk_category": self._get_risk_category(risk_score)
        }

        return risk_factors

    def _get_risk_category(self, risk_score: float) -> str:
        """Translate risk score to category"""
        if risk_score < 0.3:
            return "LOW_RISK"
        elif risk_score < 0.7:
            return "MEDIUM_RISK"
        else:
            return "HIGH_RISK"