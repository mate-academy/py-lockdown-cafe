import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("Visitor should have a vaccine!")
        if visitor.get("vaccine").get("expiration_date") is not None:
            if (datetime.date.today() > visitor
                    .get("vaccine")
                    .get("expiration_date")):
                raise OutdatedVaccineError("Vaccine is outdated!")
        if visitor.get("wearing_a_mask") is not None:
            if not visitor.get("wearing_a_mask"):
                raise NotWearingMaskError("Visitor should wear a mask!")
        return f"Welcome to {self.name}"
