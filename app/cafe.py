
import datetime
from .errors import (NotVaccinatedError,
                     OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError
        return f"Welcome to {self.name}"
