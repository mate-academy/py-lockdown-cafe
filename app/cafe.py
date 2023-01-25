import datetime

from app.errors import NotVaccinatedError, \
    NotWearingMaskError, OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        flag = [True]

        if not visitor.get("vaccine", False):
            flag.append(False)
            raise NotVaccinatedError("NotVaccinatedError")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            flag.append(False)
            raise OutdatedVaccineError("OutdatedVaccineError")

        if not visitor.get("wearing_a_mask", False):
            flag.append(False)
            raise NotWearingMaskError("NotWearingMaskError")

        if all(flag):
            return f"Welcome to {self.name}"
