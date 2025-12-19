import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        name = visitor.get("name", "Unknown Visitor")
        today = datetime.date.today()

        if "vaccine" not in visitor:
            raise NotVaccinatedError(name)

        vaccine_info = visitor["vaccine"]

        if ("expiration_date" in vaccine_info
                and vaccine_info["expiration_date"] < today):
            raise OutdatedVaccineError(name, vaccine_info["expiration_date"])

        if visitor.get("wearing_a_mask") is not True:
            raise NotWearingMaskError(name)

        return f"Welcome to {self.name}"
