import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("A visitor should be vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("A visitor should "
                                       "have up-to-date vaccine")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("A visitor should be wearing a mask")
        else:
            return f"Welcome to {self.name}"
