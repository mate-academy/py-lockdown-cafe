from datetime import date

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
            raise NotVaccinatedError("The visitor should have a 'vaccine' key")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(
                f"{visitor['name']} has out-dated vaccine"
            )
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(f"{visitor['name']} must wear a mask")
        return f"Welcome to {self.name}"
