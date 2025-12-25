import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitors: dict) -> str:
        if "vaccine" not in visitors.keys():
            raise NotVaccinatedError("Visitor should have a vaccine!")
        if visitors["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitor should update their vaccine!")
        if not visitors["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor should wear a mask!")

        return f"Welcome to {self.name}"
