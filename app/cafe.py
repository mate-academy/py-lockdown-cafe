from datetime import date
import app.errors as errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if not visitor.get("vaccine"):
            raise errors.NotVaccinatedError("Visitor should be vaccinated")

        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise errors.OutdatedVaccineError("Visitors' vaccine is expired")

        elif not visitor["wearing_a_mask"]:
            raise errors.NotWearingMaskError("Visitors should wear a mask")

        return f"Welcome to {self.name}"
