import datetime
from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(
            self,
            name: str
    ) -> None:
        self.name = name

    def visit_cafe(
            self,
            visitor: dict
    ) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor is not vaccinated")

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date and expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor has outdated vaccine")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
