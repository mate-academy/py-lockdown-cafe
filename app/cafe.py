import datetime
from .errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"Visitor {visitor['name']} "
                                     f"needs to be vaccinated "
                                     f"in order to enter "
                                     f"the {self.name}")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor['name']} "
                                       f"vaccine is expired.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor['name']} "
                                      f"cant enter without a mask on.")
        return f"Welcome to {self.name}"
