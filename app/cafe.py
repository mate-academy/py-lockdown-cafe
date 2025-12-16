import datetime

from typing import Dict, Any

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

    def visit_cafe(
            self,
            visitor: Dict[str, Any]
    ) -> str:
        vaccine_info = visitor.get("vaccine")
        if not vaccine_info:
            raise NotVaccinatedError(f"{visitor['name']} is not vaccinated.")

        if vaccine_info["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor['name']}'s "
                                       f"vaccine is outdated.")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"{visitor['name']} "
                                      f"is not wearing a mask.")

        return f"Welcome to {self.name}"
