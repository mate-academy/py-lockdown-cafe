import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("You've got no vaccine. Cant let you in.")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "Your vaccine has been expired."
                " Cant let you in"
            )
        elif (visitor["wearing_a_mask"] is False
              or visitor["wearing_a_mask"] is None):
            raise NotWearingMaskError(
                "You need to wear a mask."
                " Cant let you in without it"
            )
        else:
            return f"Welcome to {self.name}"
