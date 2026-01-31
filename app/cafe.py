import datetime
from .errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("visitor not vaccinated")

        vaccine_info = visitor["vaccine"]
        if vaccine_info["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("vaccine outdated")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("visitor dont have mask")

        return f"Welcome to {self.name}"
