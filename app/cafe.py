import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine", 0):
            raise NotVaccinatedError(f"{visitor['name']} doesn't have vaccine")

        today = datetime.date.today()
        if today > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError(
                f"{visitor['name']} does have expired vaccine"
            )

        if not visitor.get("wearing_a_mask", 0):
            raise NotWearingMaskError(
                f"{visitor['name']} doesn't have wearing mask"
            )

        return f"Welcome to {self.name}"
