import datetime
from typing import Any

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str, Any]) -> str:

        today = datetime.date.today()

        if visitor.get("vaccine"):
            if visitor["vaccine"].get("expiration_date") < today:
                raise OutdatedVaccineError(
                    f"{visitor['name']} vaccine is outdated!"
                )

        else:
            raise NotVaccinatedError(
                f"{visitor['name']} is not vaccinated!"
            )

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                f"{visitor['name']} is not wearing a mask!"
            )

        return f"Welcome to {self.name}"
