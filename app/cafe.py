from typing import Dict
import datetime
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError

class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict) -> str:
        # Перевірка, чи є ключ "vaccine"
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor.get('name', 'Visitor')} is not vaccinated")

        expiration_date = visitor["vaccine"].get("expiration_date")

        # Якщо expiration_date — рядок, конвертуємо в datetime.date
        if isinstance(expiration_date, str):
            try:
                expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d").date()
            except ValueError:
                raise OutdatedVaccineError(
                    f"{visitor.get('name', 'Visitor')}'s vaccine expiration date format is invalid"
                )
        # Якщо expiration_date не є datetime.date — помилка
        elif not isinstance(expiration_date, datetime.date):
            raise OutdatedVaccineError(
                f"{visitor.get('name', 'Visitor')}'s vaccine expiration date is invalid"
            )

        # Перевірка, чи вакцина не протермінована
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor.get('name', 'Visitor')}'s vaccine is outdated")

        # Перевірка носіння маски
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"{visitor.get('name', 'Visitor')} is not wearing a mask")

        return f"Welcome to {self.name}"
