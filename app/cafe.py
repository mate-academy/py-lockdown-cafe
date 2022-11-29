from errors import NotVaccinatedError
from errors import OutdatedVaccineError
from errors import NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name) -> None:
        self.name = name


    def visit_cafe(self, visitor: dict):
        if not visitor["vaccine"]:
            raise NotVaccinatedError
        for key in visitor.keys():
            if visitor["vaccine"] < datetime.date.today():
                raise OutdatedVaccineError
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError

        else:
            return f"Welcome to {self.name}"
