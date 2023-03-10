import datetime

from app.errors import OutdatedVaccineError, \
    NotWearingMaskError, NotVaccinatedError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Not Vaccinated")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Out dated Vaccine")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Not Wearing Mask")

        return f"Welcome to {self.name}"
