from datetime import date
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
            raise NotVaccinatedError(f"{visitor["name"]} "
                                     f"does not have vaccination")
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(f"{visitor['name']} has an "
                                       f"outdated vaccination date")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor['name']} should wear a mask")
        return f"Welcome to {self.name}"
