import datetime

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
            visitor: dict
    ) -> str | None:
        vaccine = visitor.get("vaccine", None)

        if vaccine is None:
            raise NotVaccinatedError("The visitor is not vaccinated")

        today = datetime.date.today()
        expiration = vaccine.get("expiration_date", None)
        mask = visitor.get("wearing_a_mask", None)

        if expiration is None or expiration < today:
            raise OutdatedVaccineError("The vaccine is outdated")

        if not mask:
            raise NotWearingMaskError("The visitor is not wearing mask")

        return f"Welcome to {self.name}"
