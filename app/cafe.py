import datetime
from app.errors import (NotWearingMaskError, NotVaccinatedError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You are not vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Your vaccine is outdated")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(
                f"You have to wear mask to enter a {self.name}"
            )
        return f"Welcome to {self.name}"
