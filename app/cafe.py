import datetime
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError, OutdatedVaccineError)


class Cafe:

    friend = None

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Friend should be vaccinated")
        if "vaccine" in visitor:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("Your vaccine has expired")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("You should be wearing a mask")
        else:
            return f"Welcome to {self.name}"
