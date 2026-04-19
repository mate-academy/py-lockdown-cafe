import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        today = datetime.date.today()
        exp_date = visitor["vaccine"]["expiration_date"]
        if exp_date < today:
            raise OutdatedVaccineError(
                f"Visitor’s vaccine expired on {exp_date}"
            )

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing mask")

        return f"Welcome to {self.name}"
