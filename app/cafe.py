import datetime
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"Visitor {visitor['name']} "
                f"should be vaccinated"
            )
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                f"Visitor {visitor['name']} "
                f"should visit ambulance and update his vaccine"
            )
        elif ("wearing_a_mask" not in visitor
              or visitor["wearing_a_mask"] is False):
            raise NotWearingMaskError(
                f"Visitor {visitor['name']} should be in mask"
            )
        return f"Welcome to {self.name}"
