import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError(
                "The visitor does not have a vaccine key."
            )
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "The vaccine must not be expired"
            )
        if "wearing_a_mask" not in visitor.keys() or (
                visitor["wearing_a_mask"] is False
        ):
            raise NotWearingMaskError(
                "All visitors must wear masks"
            )
        return f"Welcome to {self.name}"
