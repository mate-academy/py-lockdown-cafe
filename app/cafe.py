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
        if (visitor.get("vaccine").
                get("expiration_date") < datetime.date.today()):
            raise OutdatedVaccineError
        if ("wearing_a_mask" not in visitor
                or not visitor.get("wearing_a_mask")):
            raise NotWearingMaskError
        return f"Welcome to {self.name}"
