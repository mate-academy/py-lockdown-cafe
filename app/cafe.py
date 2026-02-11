from datetime import date, datetime

from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        exp = visitor["vaccine"]["expiration_date"]
        if isinstance(exp, str):
            exp = datetime.strptime(exp, "%Y-%m-%d").date()
        if exp < date.today():
            raise OutdatedVaccineError("Visitor's vaccine is outdated")
        if  not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor needs to wear a mask")
        return f"Welcome to {self.name}"
