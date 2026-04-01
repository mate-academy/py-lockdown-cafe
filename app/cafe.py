import datetime
from errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor):
        # Check vaccination status
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} is not vaccinated.")

        # Check vaccine expiration date
        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor['name']}'s vaccine is outdated.")

        # Check if wearing a mask
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"{visitor['name']} is not wearing a mask.")

        return f"Welcome to {self.name}"
