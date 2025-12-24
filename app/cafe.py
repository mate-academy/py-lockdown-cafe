import datetime

from app.errors import NotVaccinatedError, OutdatedVaccineError

from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitors: dict) -> str:
        if "vaccine" not in visitors:
            raise NotVaccinatedError
        if visitors["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError
        if "wearing_a_mask" not in visitors or not visitors["wearing_a_mask"]:
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
