import datetime
from .errors import (NotVaccinatedError,
                     NotWearingMaskError,
                     OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        is_ok = True
        today_date = datetime.date.today()

        if "vaccine" not in visitor or not visitor["vaccine"]:
            is_ok = False
            raise NotVaccinatedError

        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < today_date:
            is_ok = False
            raise OutdatedVaccineError

        if not visitor.get("wearing_a_mask"):
            is_ok = False
            raise NotWearingMaskError("All friends should be vaccinated")

        if is_ok:
            return f"Welcome to {self.name}"
