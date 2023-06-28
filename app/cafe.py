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
            raise NotVaccinatedError("Visitor is not vaccinated!")

        vaccine_date_info = visitor["vaccine"].get("expiration_date")
        datetime_now = datetime.date.today()

        if vaccine_date_info < datetime_now:
            raise OutdatedVaccineError("Vaccine is outdated!")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing a mask!")

        return f"Welcome to {self.name}"
