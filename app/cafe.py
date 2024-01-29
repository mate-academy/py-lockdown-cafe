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
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("All friends should be vaccinated")

        expiration_date = visitor["vaccine"]["expiration_date"]
        now = datetime.date.today()

        if expiration_date < now:
            raise OutdatedVaccineError("Visitors vaccine is expired")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Friends should buy masks")

        return f"Welcome to {self.name}"
