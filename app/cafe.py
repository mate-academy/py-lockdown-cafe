from datetime import date
from app.errors import (
    OutdatedVaccineError,
    NotVaccinatedError,
    NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            vaccine_expiration_date = visitor["vaccine"]["expiration_date"]
        except (KeyError, IndexError, TypeError):
            raise NotVaccinatedError

        if date.today() > vaccine_expiration_date:
            raise OutdatedVaccineError

        try:
            wearing_a_mask = visitor["wearing_a_mask"]
            if not wearing_a_mask:
                raise NotWearingMaskError
        except (KeyError, IndexError, TypeError):
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
