import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError()

        vaccine_info = visitor["vaccine"]

        if (
            "expiration_date" not in vaccine_info
        ) or (
            vaccine_info["expiration_date"] < datetime.date.today()
        ):
            raise OutdatedVaccineError()

        if (
            "wearing_a_mask" not in visitor
        ) or (
            not visitor["wearing_a_mask"]
        ):
            raise NotWearingMaskError()

        return f"Welcome to {self.name}"
