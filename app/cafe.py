import datetime
from app.errors import (OutdatedVaccineError,
                        NotWearingMaskError,
                        NotVaccinatedError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("NotVaccinatedError")

        visitor_date = visitor["vaccine"]["expiration_date"]

        if visitor_date < datetime.date.today():
            raise OutdatedVaccineError("OutdatedVaccineError")
        if ("wearing_a_mask" not in visitor.keys()
                or "wearing_a_mask" in visitor.keys()
                and visitor["wearing_a_mask"] is False):
            raise NotWearingMaskError("NotWearingMaskError")

        return f"Welcome to {self.name}"
