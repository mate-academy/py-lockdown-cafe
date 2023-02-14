from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        count_errors = 0
        if "vaccine" not in visitor:
            count_errors += 1
            raise NotVaccinatedError("Vaccination is missing!!")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            count_errors += 1
            raise OutdatedVaccineError("Vaccination expired")
        if visitor["wearing_a_mask"] is False:
            count_errors += 1
            raise NotWearingMaskError("Visitor should wear his mask")

        if count_errors == 0:
            return f"Welcome to {self.name}"
