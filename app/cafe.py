from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError
from datetime import date


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError

        last_date = visitor["vaccine"]["expiration_date"]
        if last_date < date.today():
            raise OutdatedVaccineError

        if visitor["wearing_a_mask"] is not True:
            raise NotWearingMaskError

        else:
            return f"Welcome to {self.name}"
