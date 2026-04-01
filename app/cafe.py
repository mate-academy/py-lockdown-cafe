from typing import Dict
import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict[str, any]) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor['name']} не вакцинирован."
            )

        vaccine_expiration_date = visitor["vaccine"]["expiration_date"]
        if vaccine_expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"Вакцина {visitor['name']} просрочена."
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{visitor['name']} не носит маску."
            )

        return f"Добро пожаловать в {self.name}"
