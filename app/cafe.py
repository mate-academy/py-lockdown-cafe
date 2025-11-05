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
        # 1. Перевірка на вакцинацію
        vaccine = visitor.get("vaccine")
        if not vaccine:
            raise NotVaccinatedError(
                f"{visitor.get("name", "Visitor")} is not vaccinated")

        expiration_date = vaccine.get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor.get("name", "Visitor")} has an outdated vaccine")

        # 2. Перевірка на маску
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{visitor.get("name", "Visitor")} is not wearing a mask")

        # 3. Якщо все гаразд
        return f"Welcome to {self.name}"
