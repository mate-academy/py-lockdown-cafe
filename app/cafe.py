import datetime
from errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} is not vaccinated.")

        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor['name']}'s vaccine is outdated. Expiration date: {expiration_date}.")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"{visitor['name']} is not wearing a mask.")

        return f"Welcome to {self.name}"
