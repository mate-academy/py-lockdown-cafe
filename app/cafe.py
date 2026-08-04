from app import errors
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        # 1. Перевірка на вакцину
        if "vaccine" not in visitor:
            raise errors.NotVaccinatedError("No vaccine")
        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise errors.OutdatedVaccineError("Vaccine expired")
        if not visitor.get("wearing_a_mask", False):
            raise errors.NotWearingMaskError("No mask")
        return f"Welcome to {self.name}"
