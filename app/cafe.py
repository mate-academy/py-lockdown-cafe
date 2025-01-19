import datetime

from app.errors import (NotWearingMaskError, OutdatedVaccineError,
                        NotVaccinatedError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        name = visitor["name"]
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError(f"{name} is not vaccinated!")
        if (visitor.get("vaccine").get("expiration_date")
                < datetime.date.today()):
            raise OutdatedVaccineError(f"{name}'s vaccine is outdated!")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"{name} is not wearing a mask!")
        return f"Welcome to {self.name}"
