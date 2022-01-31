import datetime
from app.errors import NotVaccinatedError,\
    NotWearingMaskError,\
    OutdatedVaccineError


class Cafe:
    def __init__(self, name: str):
        self.name = name
        self.today = datetime.date.today()

    def visit_cafe(self, visitor: dict):
        if "vaccine" in visitor.keys():

            if visitor["vaccine"]["expiration_date"] < self.today:
                raise OutdatedVaccineError("OutdatedVaccineError")
            elif not visitor["wearing_a_mask"]:
                raise NotWearingMaskError("NotWearingMaskError")
            else:
                return f"Welcome to {self.name}"
        else:
            raise NotVaccinatedError("NotVaccinatedError")
