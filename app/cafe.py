import datetime
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("Visitor should be vaccinated!")

        expiration_date = visitor["vaccine"]["expiration_date"]
        current_date = datetime.date.today()
        if expiration_date < current_date:
            raise OutdatedVaccineError("Outdated vaccine. "
                                       "Visitor must be vaccinated!")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(f"Visitor should buy masks")

        return f"Welcome to {self.name}"
