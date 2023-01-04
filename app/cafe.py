import datetime
from app.errors import NotVaccinatedError, \
    NotWearingMaskError, OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            visitor["vaccine"]
        except KeyError:
            raise NotVaccinatedError("All friends should be vaccinated")

        try:
            day_vaccina = visitor["vaccine"]["expiration_date"]
            today = datetime.date.today()
            if day_vaccina < today:
                raise OutdatedVaccineError("All friends should be vaccinated")
        except KeyError:
            raise OutdatedVaccineError("All friends should be vaccinated")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Need buy mask")

        return f"Welcome to {self.name}"
