from datetime import date

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        name = visitor["name"]
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"Visitor {name} must be vaccinated to visit cafe {self.name}"
            )
        expiration_date = visitor["vaccine"]["expiration_date"]
        if date.today() > expiration_date:
            raise OutdatedVaccineError(
                f"Vaccine has expired on {expiration_date} for visitor {name}"
            )
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                f"Visitor {name} must wear a mask to visit cafe {self.name}"
            )
        return f"Welcome to {self.name}"
