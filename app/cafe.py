import datetime

from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitors: dict):
        current_date = datetime.date.today()
        if "vaccine" not in visitors:
            raise NotVaccinatedError("NotVaccinatedError")
        if visitors["vaccine"].get("expiration_date") < current_date:
            raise OutdatedVaccineError("OutdatedVaccineError")
        if visitors.get("wearing_a_mask") is False:
            raise NotWearingMaskError("NotWearingMaskError")
        return f"Welcome to {self.name}"
