import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        try:
            vaccine_key = visitor["vaccine"]
            vaccine_lifetime = vaccine_key["expiration_date"]
            current_date = datetime.date.today()
            visitor_mask = visitor["wearing_a_mask"]

            if vaccine_lifetime < current_date:
                raise OutdatedVaccineError("Outdated vaccine")
            if not visitor_mask:
                raise NotWearingMaskError("Somebody is not wearing a mask")
        except KeyError:
            raise NotVaccinatedError("Somebody is not vaccinated")

        else:
            return f"Welcome to {self.name}"
