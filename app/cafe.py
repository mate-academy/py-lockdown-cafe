from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor :
            raise NotVaccinatedError("Visitor has Not Vaccinated")

        today = date.today()
        expiration = visitor["vaccine"]["expiration_date"]
        if expiration < today:
            raise OutdatedVaccineError("Visitor has Out dated Vaccine")

        if ("wearing_a_mask" not in visitor
                or visitor["wearing_a_mask"] is False):
            raise NotWearingMaskError("Visitor has Not Wearing Mask")

        return f"Welcome to {self.name}"
