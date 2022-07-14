import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError(
                f"You should be vaccinated to visit {self.name}."
            )
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "Your vaccination should not be expired."
            )
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                f"You should be wearing a mask to visit {self.name}."
            )
        return f"Welcome to {self.name}"
