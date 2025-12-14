from datetime import date
from errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError

class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor):
        # Check if the visitor has a vaccine key
        if "vaccine" not in visitor:
            raise NotVaccinatedError()

        vaccine_info = visitor["vaccine"]

        # Check if vaccine is expired
        if vaccine_info["expiration_date"] < date.today():
            raise OutdatedVaccineError()

        # Check if the visitor is wearing a mask
        if not visitor.get("wearing_mask", True):
            raise NotWearingMaskError()

        return f"Welcome to {self.name}"