import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)

today = datetime.date.today()


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("Visitor is not vaccinated!")

        if visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError(
                "The vaccine have passed its expiration date"
            )

        if (
                "wearing_a_mask"
                not in visitor.keys()
                or not visitor["wearing_a_mask"]
        ):
            raise NotWearingMaskError(
                "Visitor is not wearing a mask!"
            )

        return f"Welcome to {self.name}"
