from datetime import date
from app.errors import (
    NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Exception | str:
        flag = True
        if "vaccine" not in visitor:
            flag = False
            raise NotVaccinatedError
        elif visitor["vaccine"]["expiration_date"] < date.today():
            flag = False
            raise OutdatedVaccineError
        if not visitor["wearing_a_mask"]:
            flag = False
            raise NotWearingMaskError
        if flag:
            return f"Welcome to {self.name}"
