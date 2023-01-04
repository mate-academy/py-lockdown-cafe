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
            raise NotVaccinatedError("You are not vaccinated."
                                     " Please get vaccinated!")
        if datetime.date.today() > \
                visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("Your vaccination"
                                       " period is overdue!")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Please wear or buy a mask!")
        return f"Welcome to {self.name}"
