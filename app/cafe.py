from typing import Dict
import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict[str, str]) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError()

        vaccine_info = visitor["vaccine"]
        expiration_date = vaccine_info["expiration_date"]

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError()

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError()

        return f"Welcome to {self.name}"
