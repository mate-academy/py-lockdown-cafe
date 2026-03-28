from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        visitor_name = visitor["name"]
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor_name} not vaccinated!")
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(f"{visitor_name} vaccine "
                                       f"has expired!")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor_name} is not wearing a mask!")
        return f"Welcome to {self.name}"
