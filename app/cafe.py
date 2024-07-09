import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Exception | str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "NotVaccinatedError has occurred. "
                "Visitor has no vaccine."
            )
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "OutdatedVaccineError has occurred. "
                "Visitors vaccine is out of date"
            )
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(
                "NotWearingMaskError has occurred. "
                "Visitor have no mask"
            )
        return f"Welcome to {self.name}"
