import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        current_date = datetime.date.today()

        if "vaccine" in visitor:
            expiration_date = visitor["vaccine"]["expiration_date"]
            if expiration_date < current_date:
                raise OutdatedVaccineError("Expiration date out of time")

        if "vaccine" not in visitor:
            raise NotVaccinatedError("Not vaccinated")

        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Don't have a mask")

        return f"Welcome to {self.name}"
