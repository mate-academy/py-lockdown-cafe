import datetime

from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError")

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date is None or expiration_date < datetime.date.today():
            raise OutdatedVaccineError("OutdatedVaccineError")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("NotWearingMaskError")

        return f"Welcome to {self.name}"
