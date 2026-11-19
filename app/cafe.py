import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" in visitor.keys():
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError
        else:
            raise NotVaccinatedError
        if ("wearing_a_mask" not in visitor.keys()
                or visitor["wearing_a_mask"] is False):
            raise NotWearingMaskError
        return f"Welcome to {self.name}"
