import datetime

from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("the visitor is not vaccinated")
        expiration_date = visitor["vaccine"]["expiration_date"]
        today = datetime.date.today()
        if expiration_date < today:
            raise OutdatedVaccineError("the vaccine is expired")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("man without a mask")
        return f"Welcome to {self.name}"
