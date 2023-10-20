from errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("All friends should be vaccinated")
        elif visitor["vaccine"]["expiration_date"] > datetime.date.today():
            raise OutdatedVaccineError("Vaccine ended")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("You want buy mask")
        return f"Welcome to {self.name}"
