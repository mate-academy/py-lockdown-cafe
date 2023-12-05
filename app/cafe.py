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
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"The visitor: {visitor['name']} does not have a vaccine"
            )
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("expiration date is ended")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                f"The visitor: {visitor['name']} does not have a mask"
            )
        return f"Welcome to {self.name}"
