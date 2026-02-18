import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Exception | str:
        actual_date = datetime.date.today()
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("Vaccine information is not provided.")
        if visitor["vaccine"]["expiration_date"] < actual_date:
            raise OutdatedVaccineError("Vaccine is outdated.")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Mask must be worn.")
        return f"Welcome to {self.name}"
