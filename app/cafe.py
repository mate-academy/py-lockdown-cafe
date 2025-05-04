from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError

import datetime


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            if "vaccine" in visitor:
                expiration_date = visitor["vaccine"]["expiration_date"]
                if  expiration_date < datetime.date.today():
                    raise OutdatedVaccineError("Please make a new vaccination!")
            else:
                raise NotVaccinatedError("You have to be vaccinated.")

            if visitor["wearing_a_mask"] is False:
                raise NotWearingMaskError("To enter you should wear a mask!")
        except (NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError):
            raise
        else:
            return f"Welcome to {self.name}"
