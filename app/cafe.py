# The Cafe class should be defined in cafe.py module.
import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | Exception:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You are not vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Expired vaccination date")
        if not visitor["wearing_a_mask"] or visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("You should be wearing a mask")

        return f"Welcome to {self.name}"
