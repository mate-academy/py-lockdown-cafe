import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise (NotVaccinatedError
                   (f"Visitor {visitor['name']} is not vaccinated"))
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise (OutdatedVaccineError
                   (f"Visitor {visitor['name']}'s vaccine is outdated"))
        if not visitor["wearing_a_mask"]:
            raise (NotWearingMaskError
                   (f"Visitor {visitor['name']} doesn't have a mask"))
        return f"Welcome to {self.name}"
