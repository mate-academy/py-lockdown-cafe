from datetime import date
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All visitor should be vaccinated")
        if "expiration_date" not in visitor.get("vaccine", {}):
            raise OutdatedVaccineError("The vaccine must not be expired")
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("The vaccine must not be expired")
        elif "wearing_a_mask" not in visitor or not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("All visitors must wear masks")
        return f"Welcome to {self.name}"
