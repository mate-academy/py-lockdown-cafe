from datetime import date, datetime, timezone
from typing import Any

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def visit_cafe(
        self, visitor: dict[str, Any]
    ) -> str | NotVaccinatedError | OutdatedVaccineError | NotWearingMaskError:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Go get vaccine!")

        expiry_date: date = visitor["vaccine"]["expiration_date"]

        if expiry_date < datetime.now(tz=timezone.utc).date():
            raise OutdatedVaccineError("Go for next dose")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Grab some mask")

        return f"Welcome to {self.name}"
