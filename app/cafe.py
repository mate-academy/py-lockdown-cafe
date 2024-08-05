from datetime import date

from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine_info = visitor.get("vaccine")
        if not vaccine_info:
            raise NotVaccinatedError(f'{visitor["name"]} is not vaccinated.')

        expiration_date = vaccine_info.get("expiration_date")
        if expiration_date and expiration_date < date.today():
            raise OutdatedVaccineError(
                f'{visitor["name"]}\'s vaccine is outdated.'
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f'{visitor["name"]} is not wearing a mask.'
            )

        return f"Welcome to {self.name}"
