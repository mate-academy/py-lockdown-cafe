import datetime
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self._name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("NotVaccinatedError")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("OutdatedVaccineError")
        if visitor.get("wearing_a_mask") is not True:
            raise NotWearingMaskError("NotWearingMaskError")
        return f"Welcome to {self._name}"
