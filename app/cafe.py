from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError
import datetime


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor should be vaccinated!")
        if visitor["vaccine"]["expiration_date"] \
                < datetime.date.today():
            raise OutdatedVaccineError(
                "Visitor's vaccine should not be outdated!")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor should wear a mask!")
        return f"Welcome to {self.name}"
