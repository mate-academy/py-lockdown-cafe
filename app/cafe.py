from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
from datetime import date


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Everyone must be vaccinated")
        if date.today() > visitor["vaccine"].get("expiration_date"):
            raise OutdatedVaccineError("The vaccine must not be expired")
        if ("wearing_a_mask" not in visitor
                or visitor["wearing_a_mask"] is False):
            raise NotWearingMaskError("Everyone must wear masks")
        return f"Welcome to {self.name}"
