from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Not Vaccinated")

        elif visitor["vaccine"]["expiration_date"] \
                < datetime.date.today():

            raise OutdatedVaccineError("Out dated Vaccine")

        elif visitor["wearing_a_mask"] is False or\
                "wearing_a_mask" not in visitor:

            raise NotWearingMaskError("Not Wearing Mask")

        else:
            return f"Welcome to {self.name}"