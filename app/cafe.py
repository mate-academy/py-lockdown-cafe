import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        """
        Перевіряє, чи може відвідувач зайти в кафе.
        Очікується, що visitor — словник з ключами:
        - "vaccine": dict з ключем "expiration_date": datetime.date
        - "wearing_a_mask": bool
        """
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")

        vaccine = visitor["vaccine"]
        expiration_date = vaccine.get("expiration_date")

        if not isinstance(expiration_date, datetime.date):
            raise OutdatedVaccineError(
                "Vaccine expiration date is missing or invalid."
            )

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated.")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        return f"Welcome to {self.name}"
