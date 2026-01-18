import datetime
from errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor):
        # Check if the visitor has a vaccine key
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} is not vaccinated.")

        # Check if the vaccine is expired
        vaccine_expiration = visitor["vaccine"]["expiration_date"]
        if vaccine_expiration < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor['name']}'s vaccine has expired.")

        # Check if the visitor is wearing a mask
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"{visitor['name']} is not wearing a mask.")

        return f"Welcome to {self.name}"