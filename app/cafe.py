from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | Exception:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "Visitor should be vaccinated "
                "in order to visit our cafe."
            )
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "Vaccination date is expired! "
                "Visitor is not allowed to visit our cafe."
            )
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("All visitors should be wearing masks!")
        return f"Welcome to {self.name}"
