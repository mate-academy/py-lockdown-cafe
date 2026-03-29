import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        today = datetime.date.today()

        if "vaccine" not in visitor:
            raise NotVaccinatedError(f'{visitor["name"]} is not vaccinated.')

        if today > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError(
                f'{visitor["name"]}\'s vaccine is expired.'
            )

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f'{visitor["name"]} have to wear a mask')

        return f"Welcome to {self.name}"
