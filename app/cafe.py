import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return str(self.name)

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        elif datetime.date.today() > (
                visitor.get("vaccine").get("expiration_date")
        ):
            raise OutdatedVaccineError
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
