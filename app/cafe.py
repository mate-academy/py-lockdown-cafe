import datetime
from errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        # Check if the visitor has a vaccine key
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} is not vaccinated.")

        # Check if the vaccine is outdated
        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor['name']}'s vaccine is outdated.")

        # Check if the visitor is wearing a mask
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"{visitor['name']} is not wearing a mask.")

        # If all checks pass
        return f"Welcome to {self.name}"
