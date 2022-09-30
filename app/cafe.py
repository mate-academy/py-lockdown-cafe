import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> [NotVaccinatedError,
                                            OutdatedVaccineError,
                                            NotWearingMaskError,
                                            str]:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor does not have "
                                     "a vaccination certificate")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The visitor has an expired "
                                       "vaccination certificate")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("The visitor is not wearing a mask")
        return f"Welcome to {self.name}"
