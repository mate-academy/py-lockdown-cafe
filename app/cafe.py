import datetime
from app.exception import (
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
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f'{visitor["name"]} is not vaccinated. Access to '
                f'{self.name} denied.'
            )

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f'{visitor["name"]} has an outdated vaccine. '
                f'Access to {self.name} denied.'
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{visitor["name"]} is not wearing a mask. "
                f"Access to {self.name} denied."
            )

        return f"Welcome to {self.name}"
