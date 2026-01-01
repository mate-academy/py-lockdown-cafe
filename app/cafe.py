import datetime

from app.errors import (OutdatedVaccineError,
                        NotVaccinatedError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(f"You need to have a vaccine "
                                     f"to enter {self.name}")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Your vaccine is expired")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Please, wear a mask")
        return f"Welcome to {self.name}"
