import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor not vaccinated"
                                     " and cannot enter cafe")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitor vaccines expired")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor not wearing mask")
        return f"Welcome to {self.name}"
