from datetime import date

from app.errors import (
    OutdatedVaccineError,
    NotVaccinatedError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"Only vaccinated people can visit {self.name}"
            )
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(
                f"Visitors with expired vaccine can't visit {self.name}"
            )
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Every visitor should wear a mask")
        return f"Welcome to {self.name}"
