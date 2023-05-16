import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor isn't vaccinated")
        if ("vaccine" in visitor) and visitor["vaccine"]["expiration_date"]:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("Visitor vaccine is expired")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor doesn't wear mask")
        return f"Welcome to {self.name}"
