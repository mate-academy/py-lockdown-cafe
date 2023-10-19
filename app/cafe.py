import datetime

from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        expiration_date = visitor.get("vaccine")["expiration_date"]
        today_date = datetime.date.today()

        if expiration_date < today_date:
            raise OutdatedVaccineError("Vaccine is outdated")

        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("Visitor not wear a mask")

        return f"Welcome to {self.name}"
