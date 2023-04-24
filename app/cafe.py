import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        no_exception = True

        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError")

        today_date = datetime.date.today()
        if today_date > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("OutdatedVaccineError")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("NotWearingMaskError")

        if no_exception:
            return f"Welcome to {self.name}"
