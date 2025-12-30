import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if ("vaccine" not in visitor
                or not isinstance(visitor["vaccine"], dict)):
            raise NotVaccinatedError()
        if not isinstance(visitor["vaccine"]["expiration_date"],
                          datetime.date):
            raise OutdatedVaccineError
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError()
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError()
        return f"Welcome to {self.name}"
