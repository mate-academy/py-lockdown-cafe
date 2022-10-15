from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = datetime.date.today()
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor does not have a vaccine")
        if visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError("The vaccine is out of date")
        if "wearing_a_mask" not in visitor or not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("The visitor does not wear a mask")
        return f"Welcome to {self.name}"
