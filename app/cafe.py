import datetime

from app.errors import NotVaccinatedError
from app.errors import NotWearingMaskError
from app.errors import OutdatedVaccineError


class Cafe(object):
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get('vaccine'):
            raise NotVaccinatedError("Visitor is not vaccinated")
        expiration_date = visitor.get("vaccine", {}).get("expiration_date")
        if expiration_date and expiration_date < datetime.date.today():
            raise OutdatedVaccineError("The vaccine is outdated")
        if not visitor.get('wearing_a_mask'):
            raise NotWearingMaskError("Visitor is not wearing a mask")
        return f"Welcome to {self.name}"
