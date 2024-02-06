from datetime import date
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError, VaccineError

class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor):

        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} is not vaccinated")

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date is None or expiration_date < date.today():
            raise OutdatedVaccineError(f"{visitor['name']}'s vaccine is outdated")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"{visitor['name']} is not wearing a mask")

        return f"Welcome to {self.name}"
