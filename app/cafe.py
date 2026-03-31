import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if "vaccine" in visitor.keys():

            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("Visitor`s vaccine is expired")

        else:
            raise NotVaccinatedError("Visitor should be vaccinated")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor has no mask")

        return f"Welcome to {self.name}"
