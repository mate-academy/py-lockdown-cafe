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
        if not visitor.get("vaccine"):
            message = f"{visitor['name']} needs to be vaccinated"
            raise NotVaccinatedError(message)

        expiration_date = visitor["vaccine"].get("expiration_date")
        is_vaccinated = datetime.date.today() <= expiration_date
        if not is_vaccinated:
            message = f"{visitor['name']} has expired vaccine"
            raise OutdatedVaccineError(message)

        if not visitor.get("wearing_a_mask"):
            message = "All people should wear masks"
            raise NotWearingMaskError(message)

        return f"Welcome to {self.name}"
