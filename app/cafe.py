import datetime
from app.errors import \
    NotVaccinatedError,\
    OutdatedVaccineError,\
    NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("The person is not vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "The validity of the vaccine is not valid"
            )
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(
                "The person is without a mask"
            )
        return f"Welcome to {self.name}"
