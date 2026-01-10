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
                f"{visitor.get('name', 'Visitor')}"
                f"cannot enter "
                f"{self.name}: Not vaccinated."
            )

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date is None:
            raise OutdatedVaccineError(
                f"{visitor.get('name', 'Visitor')} cannot enter "
                f"{self.name}: Vaccine expiration date missing."
            )

        today = datetime.date.today()

        if expiration_date < today:
            raise OutdatedVaccineError(
                f"{visitor.get('name', 'Visitor')} cannot enter "
                f"{self.name}: Vaccine expired on {expiration_date}."
            )

        if visitor.get("wearing_a_mask") is not True:
            raise NotWearingMaskError(
                f"{visitor.get('name', 'Visitor')} "
                f"cannot enter "
                f"{self.name}: Must wear a mask."
            )
        return f"Welcome to {self.name}"
