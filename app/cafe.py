from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError
from datetime import date


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor.get('name', 'Visitor')} is not vaccinated")

        last_date = visitor["vaccine"]["expiration_date"]
        if last_date < date.today():
            raise OutdatedVaccineError("Vaccine has expired")

        if "wearing_a_mask" not in visitor:
            raise NotWearingMaskError(
                f"{visitor.get('name', 'Visitor')} is not wearing a mask")
        if visitor["wearing_a_mask"] is not True:
            raise NotWearingMaskError(
                f"{visitor.get('name', 'Visitor')} is not wearing a mask")

        else:
            return f"Welcome to {self.name}"
