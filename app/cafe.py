import datetime
from app.erros import NotVaccinatedError, OutdatedVaccineError, VaccineError, NotWearingMaskError

class Cafe:

    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if "vaccine" not in visitor:
            raise NotVaccinatedError("Vacina expirada")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vacina expirada")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Vacina expirada")

        return f"Welcome to {self.name}"