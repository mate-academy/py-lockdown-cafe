from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError, NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today_date = datetime.date.today()

        if "vaccine" not in visitor:
            raise NotVaccinatedError

        expiration_date = visitor.get("vaccine")["expiration_date"]
        if expiration_date < today_date:
            raise OutdatedVaccineError

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
