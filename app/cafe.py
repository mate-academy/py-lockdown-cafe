import datetime


from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Not vaccinated")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Out dated vaccine")

        if ("wearing_a_mask"
                not in visitor or visitor["wearing_a_mask"] is False):
            raise NotWearingMaskError("Not wearing mask")

        return f"Welcome to {self.name}"
