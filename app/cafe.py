from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
    VaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(
            self,
            visitor: dict
    ) -> VaccineError | NotWearingMaskError | str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All friends should be vaccinated")
        if date.today() > visitor.get("vaccine").get("expiration_date"):
            raise OutdatedVaccineError("All friends should be vaccinated")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("You aren't wearing a mask")
        return f"Welcome to {self.name}"
