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
            raise NotVaccinatedError(
                f"Visitor {visitor['name']} has no vaccine"
            )

        if visitor["vaccine"]["expiration_date"] < self.today:
            raise OutdatedVaccineError(
                f"Visitor {visitor['name']} has outdated vaccine"
            )
        if not ("wearing_a_mask" in visitor and visitor["wearing_a_mask"]):
            raise NotWearingMaskError(
                f"Visitor {visitor['name']} has no mask"
            )

        return f"Welcome to {self.name}"
