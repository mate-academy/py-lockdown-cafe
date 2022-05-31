from app.errors import \
    NotVaccinatedError, \
    OutdatedVaccineError, \
    NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError
        date_today = datetime.date.today()
        if visitor["vaccine"]["expiration_date"] < date_today:
            raise OutdatedVaccineError
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError
        else:
            return f"Welcome to {self.name}"
