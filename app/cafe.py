from datetime import date

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError,
                        )


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Error")
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Error")
        elif visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("Error")
        return f"Welcome to {self.name}"
