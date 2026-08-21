import datetime
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError,
                        )


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Person is not vaccinated")

        now = datetime.date.today()

        if visitor["vaccine"]["expiration_date"] < now:
            raise OutdatedVaccineError("Vaccine is expired")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("All must to wear mask")

        return f"Welcome to {self.name}"
