import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "Sorry, not vaccinated visitors are not allowed."
            )

        vaccine_is_expired = (visitor["vaccine"]["expiration_date"]
                              < datetime.date.today())
        if vaccine_is_expired:
            raise OutdatedVaccineError(
                "Unfortunately, your vaccine is expired."
            )

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                "All visitors must wear masks."
            )

        return f"Welcome to {self.name}"
