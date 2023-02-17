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
            raise NotVaccinatedError(
                f"NotVaccinatedError: {visitor['name']} please get vaccinated"
            )

        if datetime.date.today() > visitor["vaccine"].get("expiration_date"):
            raise OutdatedVaccineError(
                f"OutdatedVaccineError: "
                f"{visitor['name']} please renew your vaccination pass"
            )

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(
                f"NotWearingMaskError: {visitor['name']} please wear a mask"
            )

        return f"Welcome to {self.name}"
