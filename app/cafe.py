import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:

        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("Person should be vaccinated")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine should be renewed")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Person should wear a mask")

        return (f"Welcome to {self.name}")
