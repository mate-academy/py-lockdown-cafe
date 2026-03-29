from datetime import date
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        today = date.today()

        if "vaccine" not in visitor:
            raise NotVaccinatedError(f'{visitor["name"]} is not vaccinated.')

        elif today > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError(
                f'{visitor["name"]}\'s vaccine is expired.'
            )

        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f'{visitor["name"]} should wear a mask')

        return f"Welcome to {self.name}"
