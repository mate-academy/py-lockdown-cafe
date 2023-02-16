from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not ("vaccine" in visitor):
            raise NotVaccinatedError(
                "NotVaccinatedError, Person should be vaccinated!"
            )
        if datetime.date.today() > visitor.get(
                "vaccine"
        ).get(
            "expiration_date"
        ):
            raise OutdatedVaccineError(
                "OutdatedVaccineError, Person should ne vaccinated!"
            )
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                "NotWearingMaskError, everyone should have a mask"
            )
        return f"Welcome to {self.name}"
