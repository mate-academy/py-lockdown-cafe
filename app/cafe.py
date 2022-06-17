from datetime import date

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        if date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("There are not info about vaccination")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor has not mask")

        return f"Welcome to {self.name}"
