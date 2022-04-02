from app.errors import NotVaccinatedError, \
    NotWearingMaskError, \
    OutdatedVaccineError
import datetime


class Cafe():
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("немає вакцини")
        if "wearing_a_mask" in visitor.keys() and \
                not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Без маски")
        if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("ВАКЦИНА ПРОСТРОЧЕНА")
        return f"Welcome to {self.name}"
