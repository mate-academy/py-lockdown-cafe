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
        if not ("vaccine" in visitor):
            raise NotVaccinatedError(
                f"Visitor should be vaccinated "
                f"to visit the {self.name} cafe"
            )
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                f"Visitor should have active vaccine "
                f"to visit the {self.name} cafe"
            )
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                f"Visitor should wear a mask "
                f"to visit the {self.name} cafe"
            )

        return f"Welcome to {self.name}"
