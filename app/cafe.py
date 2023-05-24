import datetime
from app.errors import (
    NotWearingMaskError,
    OutdatedVaccineError,
    NotVaccinatedError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = datetime.date.today()
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(
                f"Visitor {visitor['name']} doesnt have a vaccine!"
            )
        elif visitor.get("vaccine").get("expiration_date") < today:
            raise OutdatedVaccineError(
                f"{visitor['name']}`s vaccine has expired"
            )
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                f"Visitor {visitor['name']} isn`t wearing a mask!"
            )
        return f"Welcome to {self.name}"
