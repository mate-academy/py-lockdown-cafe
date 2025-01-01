import datetime
from app.errors import NotVaccinatedError
from app.errors import  OutdatedVaccineError
from app.errors import  NotWearingMaskError

class Cafe:
    def __init__(self, name: str) -> None :
        self.name = name

    def visit_cafe(self, visitor: dict) -> str :
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor should be vaccinated")
        expiration_date = visitor["vaccine"]["expiration_date"]
        if datetime.date.today() > expiration_date:
            raise OutdatedVaccineError("Vaccine should not be expired")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor should wear a mask")
        return f"Welcome to {self.name}"