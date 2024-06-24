from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)

import datetime


class Cafe:
    def __init__(self, cafe_name: str) -> None:
        self.cafe_name = cafe_name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        vaccine_info = visitor["vaccine"]
        expiration_date = vaccine_info["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is expired")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor's not wearing a mask")

        return f"Welcome to {self.cafe_name}"
