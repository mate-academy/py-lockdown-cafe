# app/cafe.py

import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    """Representa um café com regras de entrada durante a pandemia."""

    def __init__(self, name: str) -> None:
        """Inicializa o Cafe com um nome."""
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        """
        Verifica se um visitante pode entrar no café.

        Lança exceções se as regras não forem cumpridas.
        - NotVaccinatedError: Se o visitante não tem a chave 'vaccine'.
        - OutdatedVaccineError: Se a vacina estiver expirada.
        - NotWearingMaskError: Se o visitante não estiver usando máscara.
        """
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")

        expiration_date = visitor["vaccine"].get("expiration_date")

        if not expiration_date or expiration_date < datetime.date.today():
            # Esta linha foi quebrada para respeitar o limite de 79 caracteres
            raise OutdatedVaccineError(
                "Vaccine is outdated or expiration date is missing."
            )

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        return f"Welcome to {self.name}"
