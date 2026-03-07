import datetime

from app.errors import (
    NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        today = datetime.date.today()

        if "vaccine" not in visitor:
            raise NotVaccinatedError("Can't visit cafe without vaccine")

        data_vaccine = visitor["vaccine"]["expiration_date"]

        if data_vaccine < today:
            raise OutdatedVaccineError("Vaccine is outdated")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Can't visit cafe without wearing mask")

        return f"Welcome to {self.name}"
