from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def visit_cafe(self, visitor: dict) -> str:
        if (
            visitor.get("vaccine") is None
            or visitor["vaccine"].get("expiration_date") is None
        ):
            raise NotVaccinatedError(visitor.get("name"))

        expiration_date = visitor["vaccine"]["expiration_date"]
        if datetime.date.today() > expiration_date:
            raise OutdatedVaccineError(visitor.get("name"))

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(visitor.get("name"))

        return f"Welcome to {self.name}"
