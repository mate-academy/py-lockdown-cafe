from typing import Dict, Any
import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def visit_cafe(self, visitor: Dict[str, Any]) -> str:
        # 1. Verifica vacinação
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        expiration_date: datetime.date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated")

        # 2. Verifica máscara
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        # 3. Tudo certo
        return f"Welcome to {self.name}"
