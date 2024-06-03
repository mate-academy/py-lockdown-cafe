from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)

import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"NotVaccinatedError"
                                     f" {visitor["name"]}")
        if visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError(f"OutdatedVaccineError"
                                       f" {visitor["name"]}")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(f"NotWearingMaskError"
                                      f" {visitor["name"]}")
        return f"Welcome to {self.name}"
