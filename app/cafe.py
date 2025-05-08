import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor["name"]} is not vaccinated. "
                f"Cannot visit {self.name}."
            )

        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor["name"]}'s vaccine has expired. "
                f"Cannot visit {self.name}."
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{visitor["name"]} is not wearing a mask. "
                f"Cannot visit {self.name}."
            )

        return f"Welcome to {self.name}"
