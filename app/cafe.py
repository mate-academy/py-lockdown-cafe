import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:

        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} is not vaccined!")

        expiration_date = visitor["vaccine"].get("expiration_date")

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor['name']} "
                                       f"vaccine has expired!")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(f"{visitor['name']} "
                                      f"is not wearing mask!")

        return f"Welcome to {self.name}"
