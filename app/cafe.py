import datetime

from app.errors import NotWearingMaskError, \
    NotVaccinatedError, \
    OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("you must vaccinated")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("your vaccine is outdated")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("all visitors must weak musks")

        return f"Welcome to {self.name}"
