from datetime import date
from app.errors import (OutdatedVaccineError,
                        NotVaccinatedError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("NotVaccinatedError")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("OutdatedVaccineError")
        if "wearing_a_mask" not in visitor.keys() or \
                visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("NotWearingMaskError")

        return f"Welcome to {self.name}"
