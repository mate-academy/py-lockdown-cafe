from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError
                        )
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        data = visitor["vaccine"].get("expiration_date")
        if data < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor.get('name', 'Visitor')}'s vaccine is outdated."
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing mask")

        return f"Welcome to {self.name}"
