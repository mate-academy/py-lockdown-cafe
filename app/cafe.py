import datetime
from app.errors import NotVaccinatedError,\
    OutdatedVaccineError, NotWearingMaskError


class Cafe:

    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        today_date = datetime.date.today()
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("All visitors must be vaccinated!")
        else:
            if visitor["vaccine"]["expiration_date"] < today_date:
                raise OutdatedVaccineError("The vaccine must not be expired!")
            else:
                if not visitor["wearing_a_mask"]:
                    raise NotWearingMaskError("All visitors must wear a mask!")
                else:
                    return f"Welcome to {self.name}"
