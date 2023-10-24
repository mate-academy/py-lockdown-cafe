import datetime
import app.errors as e


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor:
            raise e.NotVaccinatedError("No vaccin")

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date and expiration_date < datetime.date.today():
            raise e.OutdatedVaccineError("Vaccine has expired!")

        if not visitor.get("wearing_a_mask", False):
            raise e.NotWearingMaskError("Visitor must be wearing a mask!")

        return f"Welcome to {self.name}"
