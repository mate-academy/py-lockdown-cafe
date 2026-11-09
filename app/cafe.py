# cafe.py
import datetime
from errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        # Verifica se o visitante possui a chave 'vaccine'
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")

        # Verifica se a data de validade da vacina está vencida
        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is outdated.")

        # Verifica se o visitante está usando máscara
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        return f"Welcome to {self.name}"
