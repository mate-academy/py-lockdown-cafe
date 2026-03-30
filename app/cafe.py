import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Occurs when you have "
                                     "not done any vaccinations")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Occurs when a vaccine is outdated")
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Occurs when you are without mask")
        return f"Welcome to {self.name}"
