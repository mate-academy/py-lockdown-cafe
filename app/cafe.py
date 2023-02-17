import datetime
from .errors import (NotVaccinatedError,
                     NotWearingMaskError,
                     OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today_date = datetime.date.today()

        if not visitor.get("vaccine"):
            raise NotVaccinatedError(f"{visitor} you must have a vaccine")

        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < today_date:
            raise OutdatedVaccineError(f"{visitor} your vaccine is expired")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"{visitor} you must buy a mask")

        return f"Welcome to {self.name}"
