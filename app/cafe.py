import datetime
from app.errors import \
    NotVaccinatedError, \
    OutdatedVaccineError, \
    NotWearingMaskError


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You should be vaccinated")
        today = datetime.date.today()
        date1 = datetime.date(today.year, today.month, today.day)
        if visitor["vaccine"]["expiration_date"] != datetime.date.today():
            date2 = visitor["vaccine"]["expiration_date"]
            if date1 > date2:
                raise OutdatedVaccineError("Your vaccine is expired")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("You should wear mask")
        return f"Welcome to {self.name}"
