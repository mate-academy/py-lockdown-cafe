import datetime
from app.errors import (
    NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = datetime.date.today()
        if "vaccine" in visitor:
            expiration_date = visitor["vaccine"]["expiration_date"]
        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError")
        else:
            expiration_date = visitor["vaccine"]["expiration_date"]
            if expiration_date < today:
                raise OutdatedVaccineError("OutdatedVaccineError")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("NotWearingMaskError")
        return f"Welcome to {self.name}"
