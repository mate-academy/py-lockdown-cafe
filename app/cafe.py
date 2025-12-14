import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError(
                f"{visitor['name']} is not vaccinated!")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor['name']} vaccine is outdated!")
        if ("wearing_a_mask" not in visitor.keys()
                or visitor["wearing_a_mask"] is False):
            raise NotWearingMaskError(
                f"{visitor['name']} is not wearing mask!")
        return f"Welcome to {self.name}"
