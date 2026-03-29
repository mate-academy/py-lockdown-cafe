from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
from datetime import date

class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name
        
    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        
        today = date.today()
        expiration_date = visitor["vaccine"]["expiration_date"]
        
        if today > expiration_date:
            raise OutdatedVaccineError
        
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError
        
        return f"Welcome to {self.name}"
