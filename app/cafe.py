import datetime
from errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def vizit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        elif visitor["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError
        else:
            return f"Welcome to {self.name}"
