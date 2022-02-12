import datetime
from app.errors import NotVaccinatedError,\
    NotWearingMaskError,\
    OutdatedVaccineError


class Cafe:
    def __init__(self, name: str):
        self.name = name
        self.today = datetime.date.today()

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("NotVaccinatedError")

        if visitor["vaccine"]["expiration_date"] < self.today:
            raise OutdatedVaccineError(
                f"Visitor {visitor['name']} has outdated vaccine"
            )
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("NotWearingMaskError")

        return f"Welcome to {self.name}"
