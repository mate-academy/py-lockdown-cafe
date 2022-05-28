import datetime
from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if not("vaccine" in visitor):
            raise \
                NotVaccinatedError(f"{visitor['name']} is not vaccinated")
        if visitor["vaccine"]['expiration_date'] < datetime.date.today():
            raise \
                OutdatedVaccineError(f"{visitor['name']}' vaccine is expired")
        if not visitor["wearing_a_mask"]:
            raise \
                NotWearingMaskError(f"{visitor['name']} is not wearing mask")
        return f"Welcome to {self.name}"
