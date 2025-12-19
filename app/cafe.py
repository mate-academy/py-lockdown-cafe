from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError(f"{visitor.get('name')}"
                                     f" don`t has Vaccine")
        if visitor.get("vaccine").get("expiration_date") < date.today():
            raise OutdatedVaccineError(f"{visitor.get('name')}"
                                       f" has expired date of vaccine")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"{visitor.get('name')}"
                                      f" has to buy a wearing mask")
        return f"Welcome to {self.name}"
