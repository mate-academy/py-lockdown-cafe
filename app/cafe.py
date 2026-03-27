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
        """Verifica vacina e máscara antes de permitir a entrada no café."""

        # Verifica se está vacinado
        if not visitor.get("vaccine"):
            msg = f"{visitor['name']} is not vaccinated!"
            raise NotVaccinatedError(msg)

        # Verifica se a vacina está vencida
        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date < datetime.date.today():
            msg = f"{visitor['name']} vaccine is outdated!"
            raise OutdatedVaccineError(msg)

        # Verifica se está usando máscara
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitante não está usando máscara")

        return f"Welcome to {self.name}"
