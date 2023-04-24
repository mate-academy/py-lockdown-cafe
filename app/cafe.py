from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("All friends should be vaccinated")

        vaccine = visitor["vaccine"]
        expiration_date = vaccine.get("expiration_date")
        if expiration_date < date.today():
            raise OutdatedVaccineError("Vaccine has expired")
        print(f"{visitor['name']} visited {self.name} cafe")

        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("All Friends should have masks")
        return f"Welcome to {self.name}"
