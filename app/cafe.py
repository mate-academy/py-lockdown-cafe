from datetime import date
from typing import Union

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Union[
        NotVaccinatedError,
        OutdatedVaccineError,
        NotWearingMaskError,
        str
    ]:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(
                "Access blocked! Unvaccinated "
                "persons are not allowed to enter!"
            )

        if date.today() > visitor["vaccine"].get("expiration_date"):
            raise OutdatedVaccineError("The vaccine has expired!")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Please wear a mask!")
        return f"Welcome to {self.name}"
