import datetime

from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        expiration_date = visitor["vaccine"]["expiration_date"]
        if isinstance(expiration_date, str):
            expiration_date = datetime.datetime.strptime(
                expiration_date,
                "%Y-%m-%d"
            ).date()

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor has outdated vaccine")
        if "wearing_a_mask" not in visitor or not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor doesn't have a mask")
        return f"Welcome to {self.name}"
