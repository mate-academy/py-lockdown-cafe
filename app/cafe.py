from datetime import date
from app.errors import (
    NotWearingMaskError,
    OutdatedVaccineError,
    NotVaccinatedError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        today = date.today()
        mask = visitor.get("wearing_a_mask")
        if not vaccine:
            raise NotVaccinatedError("Sem Vacina")
        if vaccine["expiration_date"] < today:
            raise OutdatedVaccineError("Vacina fora de validade")
        if not mask:
            raise NotWearingMaskError("Sem Máscara")
        return f"Welcome to {self.name}"
