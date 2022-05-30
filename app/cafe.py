from app import errors
import datetime


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if visitor.get("vaccine") is None:
            raise errors.NotVaccinatedError
        date_today = datetime.date.today()
        if visitor["vaccine"]["expiration_date"] < date_today:
            raise errors.OutdatedVaccineError
        if visitor["wearing_a_mask"] is False:
            raise errors.NotWearingMaskError
        else:
            return f"Welcome to {self.name}"
