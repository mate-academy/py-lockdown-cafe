import datetime

from app.errors import \
    NotWearingMaskError, \
    NotVaccinatedError, \
    OutdatedVaccineError


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = datetime.date.today()

        if "vaccine" not in visitor:
            raise NotVaccinatedError("you are not vaccinated")

        if visitor.get("vaccine").get("expiration_date") < today:
            raise OutdatedVaccineError("you are not vaccinated")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("you must be wearing masks")

        else:
            return f"Welcome to {self.name}"
