from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            error = "Visitor is not vaccinated. Entry denied."
            raise NotVaccinatedError(error)

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            error = "Visitor's vaccine has expired. Entry denied."
            raise OutdatedVaccineError(error)

        if "wearing_a_mask" not in visitor or not visitor["wearing_a_mask"]:
            error = "Visitor is not wearing a mask. Entry denied."
            raise NotWearingMaskError(error)

        return f"Welcome to {self.name}"
