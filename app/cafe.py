from datetime import datetime

from app import errors as er


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise er.NotVaccinatedError("all must be vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.today().date():
            raise er.OutdatedVaccineError("all must be vaccinated")
        if visitor["wearing_a_mask"] is not True:
            raise er.NotWearingMaskError("all must wear the mask")
        return f"Welcome to {self.name}"
