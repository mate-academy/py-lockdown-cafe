import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    name = ""

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("something 3")  # TODO: put propper error
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("something")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("something 2")
        return f"Welcome to {self.name}"


kfc = Cafe("KFC")
visitor = {
    "name": "Paul",
    "age": 23,
    "vaccine": {
        "expiration_date": datetime.date.today()
    },
    "wearing_a_mask": True
}
kfc.visit_cafe(visitor)
