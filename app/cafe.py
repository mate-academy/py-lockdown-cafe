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
            raise (
                NotVaccinatedError(f"{visitor["name"]} is not vaccinated."))

        expiration_date = visitor["vaccine"].get("expiration_date")
        if not isinstance(expiration_date, datetime.date):
            raise (
                OutdatedVaccineError(f"{visitor["name"]}'s "
                                     f"vaccine information is invalid."))

        if expiration_date < datetime.date.today():
            raise (
                OutdatedVaccineError
                (f"{visitor["name"]}'s vaccine expired "
                 f"on {expiration_date.strftime("%Y-%m-%d")}."))

        if ("wearing_a_mask" not in visitor
                or not visitor["wearing_a_mask"]):
            raise (
                NotWearingMaskError(f"{visitor["name"]} "
                                    f"is not wearing a mask."))

        return f"Welcome to {self.name}"
