import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You need to have a vaccination")
        else:
            if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
                raise OutdatedVaccineError("You need to update ur vaccine")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Go wear mask! Buy it, whatever")
        return f"Welcome to {self.name}"
