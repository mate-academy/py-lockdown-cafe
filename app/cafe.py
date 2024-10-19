from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError,
                        VaccineError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            if "vaccine" not in visitor:
                raise NotVaccinatedError("NotVaccinatedError")
            elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("OutdatedVaccineError")
            elif not visitor["wearing_a_mask"]:
                raise NotWearingMaskError("NotWearingMaskError")
            return f"Welcome to {self.name}"
        except VaccineError:
            raise
        except NotWearingMaskError:
            raise
