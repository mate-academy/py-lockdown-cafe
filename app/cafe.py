import datetime
from errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor):
        # Check if vaccinated
        if "vaccine" not in visitor:
            raise NotVaccinatedError()

        expiration_date = visitor["vaccine"].get("expiration_date")
        if not expiration_date or expiration_date < datetime.date.today():
            raise OutdatedVaccineError()

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError()

        return f"Welcome to {self.name}"
