import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "To visit the cafe you need to be vaccinated!")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "To visit the cafe your vaccine shouldn't be expired!")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                "Wear the masks before visiting the cafe!")

        return f"Welcome to {self.name}"
