import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | Exception:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("The visitor does not have a vaccine")
        if datetime.date.today() > visitor["vaccine"].get("expiration_date"):
            raise OutdatedVaccineError("The visitor has an expired vaccine")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("The visitor does not have a mask")
        return f"Welcome to {self.name}"
