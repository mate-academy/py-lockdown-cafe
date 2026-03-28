from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        vaccine = visitor.get("vaccine")
        if vaccine is None:
            raise NotVaccinatedError("Everyone should be vaccinated")
        if vaccine["expiration_date"] < date.today():
            raise OutdatedVaccineError("Need to re-vaccinate")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Put on your masks!")
        return f"Welcome to {self.name}"
