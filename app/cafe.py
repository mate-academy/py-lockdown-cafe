from datetime import date

from app.errors import NotVaccinatedError, OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(
                f"{visitor['name']} doesn't have a vaccine"
            )
        if visitor["vaccine"].get("expiration_date") < date.today():
            raise OutdatedVaccineError(
                f"{visitor['name']} vaccine is expired"
            )
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{visitor['name']} doesn't wear a mask"
            )

        return f"Welcome to {self.name}"
