import datetime

from app.errors import (NotVaccinatedError, OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("No vaccine found")
        expiration = visitor["vaccine"].get("expiration_date")
        if not expiration:
            raise NotVaccinatedError("No expiration date found for vaccine")
        today = datetime.date.today()
        if expiration < today:
            raise OutdatedVaccineError("Outdated vaccine found")
        value = visitor.get("wearing_a_mask")
        if value is not True or (not isinstance(value, bool)):
            raise NotWearingMaskError("No mask found")
        return f"Welcome to {self.name}"
