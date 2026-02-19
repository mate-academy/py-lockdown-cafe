import datetime
from .errors import (NotVaccinatedError, OutdatedVaccineError,
                     NotWearingMaskError)


class Cafe:
    """Клас кафе з перевіркою COVID-19 обмежень"""

    def __init__(self, name: str) -> None:
        """Ініціалізація кафе з назвою"""
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        """
        Перевіряє чи може відвідувач увійти в кафе

        Args:
            visitor (dict): Словник з інформацією про відвідувача

        Returns:
            str: Повідомлення про успішний вхід

        Raises:
            NotVaccinatedError: Якщо відвідувач не вакцинований
            OutdatedVaccineError: Якщо вакцина прострочена
            NotWearingMaskError: Якщо відвідувач не носить маску
        """
        # Перевірка на наявність вакцини
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        # Перевірка, що vaccine є словником і містить expiration_date
        vaccine = visitor["vaccine"]
        if not isinstance(vaccine, dict):
            raise NotVaccinatedError("Invalid vaccine data")

        if "expiration_date" not in vaccine:
            raise NotVaccinatedError("Vaccine expiration date is missing")

        # Перевірка терміну дії вакцини
        expiration_date = vaccine["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is expired")

        # Перевірка на наявність маски
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
