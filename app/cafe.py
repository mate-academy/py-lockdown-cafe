# cafe.py
import datetime
from typing import Dict
from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict[str, object]) -> str:
        # Перевірка на наявність вакцини
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Особа не вакцинована")

        # Перевірка на термін дії вакцини
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Вакцина застаріла")

        # Перевірка на наявність маски
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Особа не носить маску")

        # Якщо всі перевірки пройшли, повертається привітання
        return f"Welcome to {self.name}"
