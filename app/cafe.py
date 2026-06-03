from app.errors import NotWearingMaskError
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
import datetime


class Cafe:
    def __init__(self, name: str) -> str:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        ex_date = visitor["vaccine"]["expiration_date"]
        if ex_date < datetime.date.today():
            raise OutdatedVaccineError("Viccine is expired")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor should wear a mask")

        return f"Welcome to {self.name}"
