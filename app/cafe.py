from datetime import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError
                        )


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor should be vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.today().date():
            raise OutdatedVaccineError("All visitors should be vaccinated")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("You need a mask")
        return (f"Welcome to {self.name}")
