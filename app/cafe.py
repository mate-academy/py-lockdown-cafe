import datetime


from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | Exception:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "You can't go to the cafe without the vaccine."
            )
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "The vaccine is expired"
            )
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                "You can't go to the cafe without the wearing mask."
            )
        return f"Welcome to {self.name}"
