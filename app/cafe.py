import datetime
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError

class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if 'vaccine' not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated and cannot enter the cafe.")

        expiration_date = visitor['vaccine'].get("expiration_date")
        if expiration_date is not None and expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine has expired and cannot enter the cafe.")

        if not visitor.get('wearing_a_mask', True):
            raise NotWearingMaskError("Visitor is not wearing a mask and cannot enter the cafe.")

        return f"Welcome to {self.name}"
