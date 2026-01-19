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
        if vaccine := visitor.get("vaccine"):
            if vaccine["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError
        else:
            raise NotVaccinatedError
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError
        return f"Welcome to {self.name}"
