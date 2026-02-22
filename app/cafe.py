from errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
import datetime

class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        visitor_name = visitor.get("name", "Unknown Visitor")

        if "vaccine" not in visitor:
            raise NotVaccinatedError(visitor_name)

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date is None:
            raise KeyError("Missing 'expiration_date' in vaccine data!")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(visitor["name"], expiration_date)

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(visitor_name)

        return f"Welcome to {self.name}"
