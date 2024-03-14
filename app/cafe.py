import datetime


from app.errors import (
    NotWearingMaskError,
    OutdatedVaccineError,
    NotVaccinatedError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("NotVaccinatedError")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("OutdatedVaccineError")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("NotWearingMaskError")

        return f"Welcome to {self.name}"
