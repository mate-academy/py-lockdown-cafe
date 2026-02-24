import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        expiration_date = visitor["vaccine"]["expiration_date"]
        if isinstance(expiration_date, str):
            expiration_date = datetime.datetime.strptime(
                expiration_date,
                "%Y-%m-%d"
            ).date()

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is outdated!")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor not wearing a mask")

        return f"Welcome to {self.name}"
