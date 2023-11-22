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
        current_date = datetime.date.today()

        expiration_date = (
            visitor.get("vaccine", {}).get("expiration_date", None)
        )

        if expiration_date is not None and expiration_date < current_date:
            raise OutdatedVaccineError("Expiration date out of time")

        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Not vaccinated")

        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Don't have a mask")
        else:
            return f"Welcome to {self.name}"
