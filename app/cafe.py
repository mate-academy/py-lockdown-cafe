from datetime import date
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> dict:
        self.visitor = visitor
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "Entrance denied. You are not vaccinated.")

        today = date.today()
        if visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError(
                "Entrance denied. Your vaccine is out of date.")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                "Entrance denied. You should wear a mask.")

        return (f"Welcome to {self.name}")
