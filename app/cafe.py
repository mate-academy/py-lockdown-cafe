import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        # 1. Перевір чи є ключ "vaccine"
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor has no vaccine record")

        # 2. Перевір термін придатності вакцини
        expiration: datetime.date = visitor["vaccine"]["expiration_date"]
        if expiration < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is expired")

        # 3. Перевір маску
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
