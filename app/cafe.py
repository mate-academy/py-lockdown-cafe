import datetime

from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, \
    NotWearingMaskError


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError

        if (
                datetime.date.today() - visitor["vaccine"]["expiration_date"]
        ).days > 0:
            raise OutdatedVaccineError

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
