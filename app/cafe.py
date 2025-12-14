import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("All friends should be vaccinated")

        vaccine_info = visitor["vaccine"]
        if ("expiration_date" not in vaccine_info
                or vaccine_info["expiration_date"] < datetime.date.today()):
            raise OutdatedVaccineError(
                "Outdated or missing vaccine expiration date"
            )

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("All visitors should wear masks")

        return f"Welcome to {self.name}"
