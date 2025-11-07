import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        all_ok = True
        if "vaccine" not in visitor:
            all_ok = False
            raise NotVaccinatedError("Visitor has no vaccine.")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            all_ok = False
            raise OutdatedVaccineError("Visitor's vaccine is expired.")
        if not visitor["wearing_a_mask"]:
            all_ok = False
            raise NotWearingMaskError("Visitor should wear a mask.")
        if all_ok:
            return f"Welcome to {self.name}"
