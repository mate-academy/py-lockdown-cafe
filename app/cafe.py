from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor["name"]} should be vaccinated")

        if date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError(f"{visitor["name"]} "
                                       f"should be vaccinated")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(f"Visitor {visitor["name"]} "
                                      f"must wear masks")

        return f"Welcome to {self.name}"
