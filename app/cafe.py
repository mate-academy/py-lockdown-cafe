import datetime
from .errors import (NotVaccinatedError,
                     NotWearingMaskError,
                     OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today_date = datetime.date.today()

        if "vaccine" not in visitor or not visitor.get("vaccine"):
            raise NotVaccinatedError("You must have a vaccine")

        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < today_date:
            raise OutdatedVaccineError("Your vaccine is expired")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("You must buy and wear a mask")

        return f"Welcome to {self.name}"
