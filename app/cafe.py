import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("should be vaccinated")
        elif datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("should be vaccinated")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("should wearing a mask")
        return f"Welcome to {self.name}"
