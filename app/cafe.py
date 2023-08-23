import datetime

from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:

    def __init__(self, name: str) -> None:

        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if visitor.get("vaccine") is None:
            raise NotVaccinatedError

        current_date = datetime.date.today()
        if visitor.get("vaccine").get("expiration_date") < current_date:
            raise OutdatedVaccineError

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
