import datetime
from app.errors import NotVaccinatedError, OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Do vaccine!")

        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Make a new vaccine!")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Please wear a mask!")

        return f"Welcome to {self.name}"
