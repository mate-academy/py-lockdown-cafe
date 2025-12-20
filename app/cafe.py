import datetime

from app.errors import (OutdatedVaccineError,
                        NotWearingMaskError,
                        NotVaccinatedError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" in visitor:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("OutdatedVaccineError")
        else:
            raise NotVaccinatedError("NotVaccinatedError")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("NotWearingMaskError")

        return f"Welcome to {self.name}"
