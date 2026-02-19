import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor does not vaccinated!")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitor's certificate expired!")
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor did not wear a mask!")
        else:
            return f"Welcome to {self.name}"
