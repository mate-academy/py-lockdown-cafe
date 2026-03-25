import datetime
from typing import Any

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str, Any]) -> str:
        vaccine: dict[str, Any] | None = visitor.get("vaccine")

        if vaccine is None:
            raise NotVaccinatedError(
                f"{visitor.get('name', 'Visitor')} is not vaccinated"
            )

        expiration_date: datetime.date | None = vaccine.get("expiration_date")

        if expiration_date is None or expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor.get('name', 'Visitor')} has an outdated vaccine"
            )

        if visitor.get("wearing_a_mask") is not True:
            raise NotWearingMaskError(
                f"{visitor.get('name', 'Visitor')} is not wearing a mask"
            )

        return f"Welcome to {self.name}"
