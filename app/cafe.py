import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        """Initialize the cafe with a name."""
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        """Checks if a visitor is allowed to enter the cafe."""

        # Check if the visitor has been vaccinated
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "{} is not vaccinated.".format(visitor["name"])
            )

        # Check if the vaccine is expired
        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                "{}'s vaccine is outdated.".format(visitor["name"])
            )

        # Check if the visitor is wearing a mask
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                "{} is not wearing a mask.".format(visitor["name"])
            )

        return "Welcome to {}".format(self.name)
