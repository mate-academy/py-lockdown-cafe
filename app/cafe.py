import datetime
from app.errors import (
    OutdatedVaccineError,
    NotVaccinatedError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not ("vaccine" in visitor):
            raise NotVaccinatedError()
        elif "expiration_date" not in visitor["vaccine"]:
            raise OutdatedVaccineError()
        elif datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError()
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError()
        return f"Welcome to {self.name}"
