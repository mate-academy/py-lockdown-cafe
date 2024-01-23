import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitors: dict) -> str:
        if "vaccine" not in visitors:
            raise (NotVaccinatedError
                   (f"Visitors {visitors['name']} is not vaccinated"))
        if visitors["vaccine"]["expiration_date"] < datetime.date.today():
            raise (OutdatedVaccineError
                   (f"Visitors {visitors['name']}'s vaccine is outdated"))
        if not visitors.get("wearing_a_mask"):
            raise (NotWearingMaskError
                   (f"Visitors {visitors['name']} doesn't has a mask"))
        return f"Welcome to {self.name}"
