import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"Visitor {visitor['name']} has no vaccine"
            )

        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                f"Visitor {visitor['name']} has an outdated vaccine"
            )

        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"Visitor {visitor['name']} has no mask")

        return f"Welcome to {self.name}"
