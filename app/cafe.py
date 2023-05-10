import datetime

from .errors import (NotVaccinatedError, OutdatedVaccineError,
                     NotWearingMaskError)


class Cafe(object):
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("Visitor does not have a vaccine!")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The vaccine must not be expired!")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("All visitors must wear masks!")
        return f"Welcome to {self.name}"
