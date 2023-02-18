import datetime
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        name = visitor["name"]
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{name} without vaccine")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"{name} vaccine is outdated")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{name} without a mask (Ilona?)")
        return f"Welcome to {self.name}"
