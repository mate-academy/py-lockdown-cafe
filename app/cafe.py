import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitors: dict) -> str:
        if "vaccine" not in visitors:
            raise NotVaccinatedError
        if visitors["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError
        if not visitors.get("wearing_a_mask"):
            raise NotWearingMaskError
        return f"Welcome to {self.name}"
