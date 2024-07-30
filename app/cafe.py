from datetime import date

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        all_check = True

        if not visitor.get("vaccine"):
            all_check = False
            raise NotVaccinatedError
        if date.today() > visitor["vaccine"]["expiration_date"]:
            all_check = False
            raise OutdatedVaccineError
        if not visitor["wearing_a_mask"]:
            all_check = False
            raise NotWearingMaskError

        if all_check:
            return f"Welcome to {self.name}"


if __name__ == "__main__":
    vs = Cafe("lux")
    visitor = {
        "name": "Paul",
        "age": 23,
        "vaccine": {
            "expiration_date": date(year=2025, month=2, day=23)
        },
        "wearing_a_mask": False
    }

    print(vs.visit_cafe(visitor))
