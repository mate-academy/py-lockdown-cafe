from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError

        if "expiration_date" in visitor["vaccine"]:
            expire = visitor["vaccine"]["expiration_date"]
            if expire < datetime.date.today():
                raise OutdatedVaccineError

        if not visitor.get("wearing_a_mask", True):
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
