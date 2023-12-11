import datetime
from app.errors import (NotVaccinatedError, OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = datetime.date.today()

        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor does not have a vaccine")

        if visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError("Vaccination date is expired")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor must wear mask")

        return f"Welcome to {self.name}"
