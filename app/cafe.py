import datetime
from app.errors import (
    OutdatedVaccineError,
    NotVaccinatedError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> str:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if not ("vaccine" in visitor):
            raise NotVaccinatedError()
        elif datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError()
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError()
        return f"Welcome to {self.name}"
