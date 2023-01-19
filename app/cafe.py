from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("NotVaccinatedError")
        date1 = visitor["vaccine"]["expiration_date"]
        if date1 < datetime.date.today():
            raise OutdatedVaccineError("OutdatedVaccineError")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("NotWearingMaskError")
        return f"Welcome to {self.name}"
