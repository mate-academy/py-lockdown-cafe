from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError()

        expiration_date = visitor["vaccine"]["expiration_date"]

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError()

        wearing_a_mask = visitor["wearing_a_mask"]

        if not wearing_a_mask:
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
