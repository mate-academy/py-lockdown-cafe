from datetime import date

from app.errors import (NotVaccinatedError,
                        NotWearingMaskError, OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today_date = date.today()
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Vaccine is necessary!")
        elif visitor["vaccine"]["expiration_date"] < today_date:
            raise OutdatedVaccineError("Vaccine must be not expired!")
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Having a mask is necessary!")
        return f"Welcome to {self.name}"
