from app.errors import \
    (NotVaccinatedError,
     OutdatedVaccineError,
     NotWearingMaskError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You must be vaccinated ")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine expired")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("You must wear a mask")

        return f"Welcome to {self.name}"
