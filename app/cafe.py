from datetime import date

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f'{visitor["name"]}'
                                     f' is not vaccinated')

        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(f'{visitor["name"]}'
                                       f' vaccine expired')

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
