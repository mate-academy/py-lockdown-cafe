from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, human: dict) -> str:
        if "vaccine" not in human:
            raise NotVaccinatedError("Access denied: You are not vaccinated.")
        if human["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(
                f"Access denied: Your vaccine expired"
                f" on {human['vaccine']['expiration_date']}."
                f" Please get a new vaccination."
            )
        if human["wearing_a_mask"] is False:
            raise NotWearingMaskError("Access denied:"
                                      " You must wear a mask to enter.")
        return f"Welcome to {self.name}"
