import datetime
from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError


class Cafe:

    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if 'vaccine' not in visitor:
            raise NotVaccinatedError("Please get vaccinated "
                                     "and visit us again.")
        expiration_date = visitor["vaccine"]["expiration_date"]
        date_today = datetime.date.today()
        if expiration_date < date_today:
            raise OutdatedVaccineError("Your vaccination period has"
                                       " expired. Please get "
                                       "vaccinated and visit us again.")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("All visitors must wear masks.")
        return f"Welcome to {self.name}"
