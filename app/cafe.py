import datetime
import app.errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise app.errors.NotVaccinatedError(
                "Visitor is not vaccinated."
            )
        exp = visitor.get(
            "vaccine", {}).get("expiration_date"
                               )
        if exp is None:
            raise app.errors.NotVaccinatedError(
                "Visitor is not vaccinated."
            )
        if exp < datetime.date.today():
            raise app.errors.OutdatedVaccineError(
                f"Vaccine expired on {exp}"
            )
        if not visitor.get("wearing_a_mask", False):
            raise app.errors.NotWearingMaskError(
                "Visitor is not wearing a mask"
            )
        return f"Welcome to {self.name}"
