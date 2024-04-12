from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vac = visitor.get("vaccine")
        if vac is None:
            raise NotVaccinatedError(f"{visitor["name"]}: No vaccine provided")

        current_date = datetime.date.today()
        expiration_date = vac.get("expiration_date")
        if current_date > expiration_date:
            raise OutdatedVaccineError(f"{visitor["name"]}: Vaccine expired")

        wearing_mask = visitor.get("wearing_a_mask")
        if wearing_mask is not True:
            raise NotWearingMaskError(f"{visitor["name"]}: No mask provided")

        return f"Welcome to {self.name}"
