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
            raise NotVaccinatedError(f"{visitor['name']} "
                                     f"does not have vaccine. "
                                     f"Not allowed to entry")
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(f"{visitor['name']}'s "
                                       f"vaccine is expired. "
                                       f"Not allowed to entry")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(f"{visitor['name']} "
                                      f"should buy a mask before visiting "
                                      f"{self.name}")
        else:
            return f"Welcome to {self.name}"
