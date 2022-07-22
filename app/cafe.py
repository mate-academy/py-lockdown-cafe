import datetime

from app import errors


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        today = datetime.date.today()

        if "vaccine" not in visitor:
            raise errors.NotVaccinatedError("Person is not vaccinated")

        if today > visitor["vaccine"]["expiration_date"]:
            raise errors.OutdatedVaccineError("The vaccine had expired")

        if not visitor["wearing_a_mask"]:
            raise errors.NotWearingMaskError("The visitor without mask")

        return f"Welcome to {self.name}"
