import datetime
from errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError

class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitors are required to be vaccinated.")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitors are required to wear a face mask.")

        vaccine_info = visitor["vaccine"]
        expiration_date = vaccine_info.get("expiration_date")
        if not isinstance(expiration_date, datetime.date):
            raise ValueError("Invalid or missing expiration date in vaccine information.")

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("The visitor's vaccine is expired.")

        return f"Welcome to {self.name}"
