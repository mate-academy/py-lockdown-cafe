from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"Visitor {visitor['name']} isn't vaccinated"
            )
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(
                f"Visitor {visitor['name']} has expired vaccine"
            )
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                f"Visitor {visitor['name']} isn't wearing mask"
            )

        return f"Welcome to {self.name}"
