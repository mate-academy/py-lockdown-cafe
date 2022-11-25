from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError
from datetime import date


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All friends should be vaccinated")

        elif visitor["vaccine"]["expiration_date"] \
                < date.today():

            raise OutdatedVaccineError("Vaccine shouldn't be out of dated ")

        elif visitor["wearing_a_mask"] is False or \
                "wearing_a_mask" not in visitor:

            raise NotWearingMaskError("Friends should buy masks")
        return f"Welcome to {self.name}"
