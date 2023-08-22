import datetime
from app.errors import (
    NotWearingMaskError,
    OutdatedVaccineError,
    NotVaccinatedError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("The visitor does not have vaccine key")

        if datetime.date.today() > visitor["vaccine"].get("expiration_date"):
            raise OutdatedVaccineError("The visitor's vaccine has expired")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("The visitor is not wearing the mask")

        return f"Welcome to {self.name}"
