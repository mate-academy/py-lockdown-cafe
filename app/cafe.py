import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError(f"{visitor['name']} is not vaccinated")
        if visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor['name']} have a outdated vaccine"
            )
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"{visitor['name']} have no masks")

        return f"Welcome to {self.name}"
