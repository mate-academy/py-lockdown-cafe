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
                f"Visitor {visitor['name']} has no record of vaccination."
            )

        expiration_date = visitor["vaccine"].get("expiration_date")

        if datetime.date.today() > expiration_date:
            raise OutdatedVaccineError(
                f"Visitor {visitor['name']} cannot visit the cafe "
                "because he has an outdated vaccination record."
            )

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                f"Visitor {visitor['name']} cannot visit the cafe "
                "because he/she does not have a face mask."
            )

        return (f"Welcome to {self.name}")
