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
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor has no vaccine info")

        expiration_date = visitor["vaccine"]["expiration_date"]
        today = datetime.date.today()

        if expiration_date < today:
            raise OutdatedVaccineError("vaccine is expired")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("There is no wearing mask")

        return f"Welcome to {self.name}"
