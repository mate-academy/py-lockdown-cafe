import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("You've got no vaccine. Cant let you in.")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "Your vaccine has been expired."
                " Cant let you in"
            )
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                "You need to wear a mask."
                " Cant let you in without it"
            )
        return f"Welcome to {self.name}"
