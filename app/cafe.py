import datetime
from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} is not vaccinated!")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor['name']}'s"
                                       f" vaccine is expired!")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Everyone should wear a mask!")
        return f"Welcome to {self.name}"
