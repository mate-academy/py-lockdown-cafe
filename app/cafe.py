# app/cafe.py
import datetime
from typing import Dict
from .errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:  # ANN001
        self.name = name

    def visit_cafe(self, visitor: Dict) -> str:  # ANN001, ANN201
        today = datetime.date.today()

        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f'Посетитель {visitor.get("name", "N/A")} не вакцинирован.'
            )

        vaccine_info = visitor["vaccine"]

        if ("expiration_date" in vaccine_info
                and vaccine_info["expiration_date"] < today):
            raise OutdatedVaccineError(
                f'Вакцина посетителя {visitor.get("name", "N/A")} истекла '
                f'({vaccine_info["expiration_date"]}).'
            )

        if visitor.get("wearing_a_mask") is not True:
            raise NotWearingMaskError(
                f'Посетитель {visitor.get("name", "N/A")} не носит маску.'
            )

        return f"Welcome to {self.name}"
