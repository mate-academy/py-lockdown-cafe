import datetime
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str, int | str]) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError()
        if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError
        if (not visitor.get("wearing_a_mask")
                or visitor["wearing_a_mask"] is False):
            raise NotWearingMaskError
        return f"Welcome to {self.name}"
