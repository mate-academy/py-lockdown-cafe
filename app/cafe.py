import datetime

from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError, VaccineError


class Cafe:
    today_date = datetime.date.today()
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self,visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        if visitor["vaccine"]["expiration_date"] < self.today_date:
            raise OutdatedVaccineError("Visitor's vaccine is outdated")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitors not wearing mask")

        return f"Welcome to {self.name}"

