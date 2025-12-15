import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor['name']} should be vaccinated!"
            )

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor['name']}'s vaccine is outdated!"
            )

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(
                f"{visitor['name']} isn't wearing a mask!"
            )

        return f"Welcome to {self.name}"
