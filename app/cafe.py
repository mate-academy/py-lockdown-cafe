from datetime import date
from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if not visitor.get("vaccine"):
            raise NotVaccinatedError

        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
