import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(
            self,
            name: str
    ) -> None:
        self.name = name

    def visit_cafe(
            self,
            visitor: dict
    ) -> str:
        vaccine = visitor.get("vaccine")

        if vaccine is None:
            raise NotVaccinatedError(
                "The visitor is not vaccinated"
            )

        today = datetime.date.today()
        expiration = vaccine.get("expiration_date")
        mask = visitor.get("wearing_a_mask")

        if expiration is None or expiration < today:
            raise OutdatedVaccineError(
                "The vaccine is outdated"
            )

        if not mask:
            raise NotWearingMaskError("The visitor is not wearing mask")

        return f"Welcome to {self.name}"
