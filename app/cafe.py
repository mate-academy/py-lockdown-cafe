import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(
            self,
            name: str
    ) -> None:
        self.name = name

    def visit_cafe(
            self,
            visitor: dict
    ) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("Visitor is not vaccinated")

        expiration_raw = visitor["vaccine"].get("expiration_date")

        if expiration_raw is None:
            raise OutdatedVaccineError("Vaccine has no expiration date")

        if isinstance(expiration_raw, str):
            expiration = datetime.date.fromisoformat(expiration_raw)
        else:
            expiration = expiration_raw

        if expiration < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
