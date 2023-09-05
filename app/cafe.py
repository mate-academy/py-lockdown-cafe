import datetime

from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The person is not vaccinated")

        expiration_date = visitor["vaccine"].get("expiration_date")

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine has expired")

        if "wearing_a_mask" in visitor and not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("The person is not wearing a mask")

        return f"Welcome to {self.name}"
