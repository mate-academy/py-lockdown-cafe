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
                "{} not vaccinated.".format(visitor.get("name", "Visitor"))
            )
        if "expiration_date" not in visitor["vaccine"]:
            raise OutdatedVaccineError(
                "Vaccine expiration date missing."
            )

        if not isinstance(
            visitor["vaccine"]["expiration_date"], datetime.date
        ):
            raise OutdatedVaccineError(
                "Wrong date format."
            )

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated.")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                "{} is not wearing a mask.".format(
                    visitor.get("name", "Visitor")
                )
            )

        return f"Welcome to {self.name}"
