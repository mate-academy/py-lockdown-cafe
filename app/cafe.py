import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Go do vaccine!")
        else:
            if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
                raise OutdatedVaccineError("Go do vaccine!")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Go wear mask!")
        return f"Welcome to {self.name}"
