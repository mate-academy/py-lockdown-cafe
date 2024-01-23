import datetime

from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("Cannot access without a vaccine")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Cannot access with an outdated vaccine")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Cannot access without mask")

        return f"Welcome to {self.name}"
