import datetime
from app.errors import (
    OutdatedVaccineError,
    NotVaccinatedError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date and expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine "
                                       "information is missing."
                                       )

        if (visitor["wearing_a_mask"] is False
                and not visitor["wearing_a_mask"]):
            raise NotWearingMaskError("There is no mask, please wear a mask")
        return f"Welcome to {self.name}"
