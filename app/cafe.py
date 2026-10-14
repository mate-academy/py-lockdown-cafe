from datetime import date
from app.errors import NotVaccinatedError, OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        vaccine = visitor.get("vaccine")
        if not vaccine:
            raise NotVaccinatedError("Visitor is not vaccinated")

        if vaccine.get("expiration_date") < date.today():
            raise OutdatedVaccineError("Vaccine is outdated")
