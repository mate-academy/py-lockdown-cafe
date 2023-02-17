import datetime

from app.errors import (OutdatedVaccineError,
                        NotVaccinatedError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitors: dict) -> str:
        if "vaccine" not in visitors:
            raise NotVaccinatedError("You must be vaccinated")
        if visitors["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The vaccine you received is outdated.")
        if not visitors["wearing_a_mask"]:
            raise NotWearingMaskError("You must wear a mask")
        return f"Welcome to {self.name}"
