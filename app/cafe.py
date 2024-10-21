import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)
from typing import Dict


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def check_entry_requirements(self, visitor: Dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError()

        vaccine = visitor["vaccine"]
        expiration_date = vaccine.get("expiration_date")

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError()

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError()

        return f"Welcome to {self.name}"
