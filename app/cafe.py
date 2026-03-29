import datetime
from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor does not contain a vaccine")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitor vaccine is outdated")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("visitor does not "
                                      "contain a wearing a_mask")
        return f"Welcome to {self.name}"
