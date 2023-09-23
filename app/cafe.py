from app.errors import (NotWearingMaskError,
                        OutdatedVaccineError,
                        NotVaccinatedError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError(" ")

        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(" ")

        elif visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError(" ")

        return f"Welcome to {self.name}"
