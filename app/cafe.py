import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor["name"]} isn't vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor["name"]}'s vaccine is outdated')")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"{visitor["name"]} dont have mask")
        return f"Welcome to {self.name}"
