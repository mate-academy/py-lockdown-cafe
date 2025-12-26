from __future__ import annotations
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            vaccine_info = visitor["vaccine"]
        except KeyError:
            raise NotVaccinatedError
        try:
            expiration_date = vaccine_info["expiration_date"]
            if expiration_date < datetime.date.today():
                raise OutdatedVaccineError
        except KeyError:
            raise NotVaccinatedError

        try:
            if not visitor["wearing_a_mask"]:
                raise NotWearingMaskError
        except KeyError:
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
