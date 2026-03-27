import datetime

from app.errors import (
    OutdatedVaccineError,
    NotVaccinatedError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} is not vaccinated.")

        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor['name']} has an outdated"
                                       f"vaccine.")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"{visitor['name']} is not wearing"
                                      f"a mask.")

        return f"Welcome to {self.name}"
