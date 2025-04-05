from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError")
        expiration_date = visitor["vaccine"]["expiration_date"]
        today_date = datetime.date.today()
        if expiration_date < today_date:
            raise OutdatedVaccineError("OutdatedVaccineError")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("NotWearingMaskError")
        else:
            return f"Welcome to {self.name}"
