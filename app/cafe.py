import datetime

from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError, NotWearingMaskError


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f'{visitor["name"]} has no vaccine')
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f'{visitor["name"]}"s'
                                       + " vaccine is expired")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f'{visitor["name"]}'
                                      + " is not wearing a mask")

        return f"Welcome to {self.name}"
