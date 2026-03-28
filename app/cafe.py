from datetime import date
from errors import VaccineError, NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError



class Cafe:
    def __init__(self, name: str) -> None :
        self.name = name


    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError
        return f"Welcome to {self.name}"