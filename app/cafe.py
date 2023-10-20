import app.errors
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise app.errors.NotVaccinatedError("All friends should be vaccinated")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise app.errors.OutdatedVaccineError("Vaccine ended")
        elif not visitor["wearing_a_mask"]:
            raise app.errors.NotWearingMaskError("You want buy mask")
        return f"Welcome to {self.name}"
