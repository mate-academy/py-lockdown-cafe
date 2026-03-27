import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


current_date = datetime.date.today()


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        if visitor["vaccine"]["expiration_date"] < current_date:
            raise OutdatedVaccineError(
                f"Vaccine expired on "
                f"{visitor["vaccine"]["expiration_date"]}"
            )
        if (
                not visitor.get("wearing_a_mask")
                or visitor["wearing_a_mask"] is False
        ):
            raise NotWearingMaskError("Expected wearing a mask")
        return f"Welcome to {self.name}"
