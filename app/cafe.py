import datetime

from app.errors import (NotVaccinatedError, OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(f"Visitor {visitor["name"]} "
                                     f"doesn't have a vaccine!")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"Visitor {visitor["name"]} "
                                       f"has an expired vaccine!")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"Visitor {visitor["name"]} "
                                      f"doesn't have a mask!")

        return f"Welcome to {self.name}"
