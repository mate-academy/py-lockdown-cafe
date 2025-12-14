from dataclasses import dataclass
from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


@dataclass
class Cafe:
    name: str

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f'{visitor["name"]} should be vaccinated')

        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(
                f'{visitor["name"]}\'s vaccine is outdated'
            )

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f'{visitor["name"]} should wear a mask')

        return f"Welcome to {self.name}"
