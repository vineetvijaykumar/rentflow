# app/services/payment_scheduler.py
from typing import List, Dict
from datetime import datetime, timedelta


class PaymentScheduler:
    def create_flexible_schedule(
            self,
            total_rent: float,
            monthly_income: float
    ) -> Dict[str, List[Dict[str, float]]]:
        """
        Generate a flexible payment schedule based on income and total rent

        Args:
            total_rent (float): Total monthly rent amount
            monthly_income (float): User's monthly income

        Returns:
            Dict containing payment schedule details
        """
        # Determine number of installments based on income
        num_installments = self._calculate_installments(monthly_income)

        # Calculate installment amounts
        installments = self._split_payments(
            total_rent,
            num_installments
        )

        return {
            "total_rent": total_rent,
            "num_installments": num_installments,
            "installments": installments
        }

    def _calculate_installments(self, monthly_income: float) -> int:
        """
        Determine number of installments based on income

        Rules:
        - Minimum 2 installments
        - Maximum 5 installments
        - More flexible for higher incomes
        """
        if monthly_income < 2000:
            return 2
        elif monthly_income < 4000:
            return 3
        elif monthly_income < 6000:
            return 4
        else:
            return 5

    def _split_payments(
            self,
            total_rent: float,
            num_installments: int
    ) -> List[Dict[str, float]]:
        """
        Split total rent into installments with slight variations

        Args:
            total_rent (float): Total rent amount
            num_installments (int): Number of payment splits

        Returns:
            List of installment details
        """
        base_installment = total_rent / num_installments

        installments = []
        remaining = total_rent

        for i in range(num_installments):
            # Add small variation to installments
            variation = base_installment * (0.05 if i % 2 == 0 else -0.05)
            installment_amount = base_installment + variation

            # Adjust last installment to match exact total
            if i == num_installments - 1:
                installment_amount = remaining

            installments.append({
                "installment_number": i + 1,
                "amount": round(installment_amount, 2),
                "suggested_date": self._suggest_payment_date(i, num_installments)
            })

            remaining -= installment_amount

        return installments

    def _suggest_payment_date(
            self,
            installment_index: int,
            total_installments: int
    ) -> str:
        """
        Suggest payment dates spread across the month

        Args:
            installment_index (int): Current installment number
            total_installments (int): Total number of installments

        Returns:
            Suggested payment date as string
        """
        today = datetime.now()
        days_in_month = 30  # Simplified

        suggested_day = 1 + (installment_index * (days_in_month // total_installments))
        suggested_date = today.replace(day=suggested_day)

        return suggested_date.strftime("%Y-%m-%d")