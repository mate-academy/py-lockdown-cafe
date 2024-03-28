from app import errors
from datetime import date


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if not visitor.get("vaccine"):
            raise errors.NotVaccinatedError(
                f"{visitor['name']} is not vaccinated!"
            )

        if date.today() > visitor["vaccine"]["expiration_date"]:
            raise errors.OutdatedVaccineError(
                f"Outdated vaccine for {visitor['name']}"
            )

        if not visitor.get("wearing_a_mask") is True:
            raise errors.NotWearingMaskError(
                f"{visitor['name']} not wearing the Mask"
            )

        return f"Welcome to {self.name}"
