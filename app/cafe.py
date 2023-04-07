from datetime import date, datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str, int, bool, datetime]) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError")
        if date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("OutdatedVaccineError")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("NotWearingMaskError")
        return f"Welcome to {self.name}"
