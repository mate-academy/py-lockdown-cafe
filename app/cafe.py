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
    ) -> VaccineError | NotWearingMaskError | str:

        if "vaccine" not in visitor:
            raise NotVaccinatedError("This visitor is no vaccinated!")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("This visitor has expired vaccine!")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("This visitor doesn't have a mask!")

        return f"Welcome to {self.name}"
