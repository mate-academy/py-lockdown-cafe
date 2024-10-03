from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError,
)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine"):
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("OutdatedVaccineError")
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("NotVaccinatedError")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("NotWearingMaskError")
        return f"Welcome to {self.name}"


if __name__ == "__main__":
    kfc = Cafe("KFC")
    visitor = {
        "name": "Paul",
        "age": 23,
        "vaccine": {
            "expiration_date": datetime.date.today()
        },
        "wearing_a_mask": False
    }
    print(kfc.visit_cafe(visitor))
