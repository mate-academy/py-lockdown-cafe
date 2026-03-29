import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "{} is not vaccinated.".format(visitor["name"])
            )
        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date is None or expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                "{}'s vaccine is outdated or missing an expiration date."
                .format(visitor["name"])
            )
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                "{} is not wearing a mask.".format(visitor["name"])
            )
        return "Welcome to {}".format(self.name)
