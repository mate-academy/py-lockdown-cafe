from datetime import date

from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Go get a Vaccine")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Vaccine is not valid go get a new one")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Feel free to buy a mask")
        else:
            return f"Welcome to {self.name}"
