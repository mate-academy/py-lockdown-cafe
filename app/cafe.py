import datetime

from app.errors import (
    VaccineError,
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(
            self,
            visitor: dict
    ) -> str | VaccineError | OutdatedVaccineError:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("visitor is not vaccinated")
        if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("the vaccine is expired")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("the visitor does not have a mask")
        return f"Welcome to {self.name}"
