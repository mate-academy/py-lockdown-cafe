from datetime import date

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        name = visitor["name"]

        if visitor.get("vaccine") is None:
            raise NotVaccinatedError(name)

        vaccine = visitor["vaccine"]

        if self.is_outdated(vaccine["expiration_date"]):
            raise OutdatedVaccineError(name)

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(name)

        return f"Welcome to {self.name}"

    @staticmethod
    def is_outdated(expiration_date: date) -> bool:
        return date.today() > expiration_date
