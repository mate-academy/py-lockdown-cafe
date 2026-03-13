from datetime import date

from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"No vaccine for {self.name}")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(f"Outdated vaccine for {self.name}")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"Not Wearing Mask for {self.name}")

        return f"Welcome to {self.name}"
