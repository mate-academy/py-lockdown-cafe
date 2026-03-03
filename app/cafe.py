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
        vaccine = visitor.get("vaccine")

        if not vaccine:
            raise NotVaccinatedError(
                f'{visitor.get("name", "Visitor")} must be vaccinated'
            )

        vaccine_date = vaccine.get("expiration_date")

        if not vaccine_date or vaccine_date < datetime.date.today():
            raise OutdatedVaccineError(
                f'{visitor.get("name", "Visitor")}s vaccine is outdated'
            )

        wearing_a_mask = visitor.get("wearing_a_mask")

        if not wearing_a_mask:
            raise NotWearingMaskError(
                f"{visitor.get('name', 'Visitor')} must wear the mask"
            )

        return f"Welcome to {self.name}"
