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
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("The visitor should have a 'vaccine' key")
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("The 'vaccine' key is out-dated")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("All visitors must wear masks")
        else:
            return f"Welcome to {self.name}"
