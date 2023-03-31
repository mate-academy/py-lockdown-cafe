import datetime
from app.errors import OutdatedVaccineError
from app.errors import NotVaccinatedError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("All friends should be vaccinated")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The vaccine must not be expired")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("All friends should wearing a mask")
        return f"Welcome to {self.name}"
