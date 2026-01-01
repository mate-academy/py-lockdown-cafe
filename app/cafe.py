import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Person is not vaccinated!")

        elif visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError("the vaccine for visitors is outdated")

        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Need to buy a face mask!")

        return f"Welcome to {self.name}"
