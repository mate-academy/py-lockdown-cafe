from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor should be vaccinated")

        today = datetime.date.today()
        if visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError("Vaccine is outdated")

        if "wearing_a_mask" not in visitor or visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor should wear a mask")

        return f"Welcome to {self.name}"
