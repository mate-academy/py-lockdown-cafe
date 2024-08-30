import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(
            self,
            name: str
    ) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        name_of_visitor = visitor["name"]
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{name_of_visitor} is not vaccinated. Access to "
                f"{self.name} denied."
            )

        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"{name_of_visitor} has an outdated vaccine. "
                f"Access to {self.name} denied."
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{name_of_visitor} is not wearing a mask. "
                f"Access to {self.name} denied."
            )

        return f"Welcome to {self.name}"
