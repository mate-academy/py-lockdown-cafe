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

        vaccine = visitor.get("vaccine", None)
        visitor_name = visitor["name"]

        if not vaccine:
            raise NotVaccinatedError(
                f"{visitor_name}"
                f" is not vaccinated and cannot enter"
            )

        vaccine_info = visitor["vaccine"]

        expiration_date = vaccine_info.get("expiration_date")
        if expiration_date and expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor_name}'s vaccine expired on "
                f"{expiration_date}. It is outdated."
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"{visitor_name} "
                                      f"must be wearing a mask to enter.")

        return f"Welcome to {self.name}"
