from datetime import date
from app.errors import (NotVaccinatedError,
                    OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def _is_vaccine_valid(self, vaccine: dict) -> bool:
        return vaccine["expiration_date"] >= date.today()

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor does not have a vaccine key.")
        if not self._is_vaccine_valid(visitor["vaccine"]):
            raise OutdatedVaccineError("Vaccine has expired.")
        if "mask" not in visitor or not visitor["mask"]:
                raise NotWearingMaskError("Visitor is not wearing a mask.")
        return f"Welcome to {self.name}"
