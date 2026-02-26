import datetime
from app.errors import (
    NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        # Перевірка наявності ключа vaccine
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")

        # Перевірка дати закінчення дії вакцини
        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated.")

        # Перевірка наявності маски
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                "Visitor is not wearing a mask.")

        # Усі правила дотримані
        return f"Welcome to {self.name}"
