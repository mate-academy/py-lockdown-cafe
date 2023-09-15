import datetime

from app.errors import (OutdatedVaccineError,
                        NotVaccinatedError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        date_today = datetime.date.today()
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("NotVaccinatedError")
        if visitor["vaccine"]["expiration_date"] < date_today:
            raise OutdatedVaccineError("OutdatedVaccineError")
        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("NotWearingMaskError")
        else:
            return f"Welcome to {self.name}"
