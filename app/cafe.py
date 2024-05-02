import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if not visitor.get("vaccine"):
            raise NotVaccinatedError("a vaccination certificate must be")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("the vac_certificate is not valid")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("entrance only with masks")

        return f"Welcome to {self.name}"
