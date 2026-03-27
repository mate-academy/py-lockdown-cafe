import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Someone not vaccineted")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Someone`s vaccine is outdated")
        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("Someone haven`t mask -_0")
        return f"Welcome to {self.name}"
