from datetime import date

import app.errors as error


class Cafe:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise error.NotVaccinatedError("Visitor must be vaccinated")

        if visitor["vaccine"]["expiration_date"] < date.today():
            raise error.OutdatedVaccineError("Vaccination is outdated")

        if not visitor["wearing_a_mask"]:
            raise error.NotWearingMaskError("Visitor not wearing the mask")

        return f"Welcome to {self.name}"
