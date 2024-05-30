import datetime

from app.errors import (NotWearingMaskError, OutdatedVaccineError,
                        NotVaccinatedError)


class Cafe:
    def __init__(self, name: str) -> None:
        self._name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor has to be vaccinated.")
        today = datetime.date.today()
        if today > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("The visitor's vaccine date "
                                       "is out of date.")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("The visitor doesn't wear a mask.")
        return f"Welcome to {self._name}"

    @property
    def name(self) -> str:
        return self._name
