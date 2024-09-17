from datetime import date

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor} isn't vaccinated")
        if date.today() > visitor.get("vaccine")["expiration_date"]:
            raise OutdatedVaccineError(f"{visitor} have outdated vaccine")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"{visitor} doesn't have a mask")

        return f"Welcome to {self.name}"
