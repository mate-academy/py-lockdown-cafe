import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError()

        vaccine_info = visitor["vaccine"]
        expiration_date = vaccine_info.get("expiration_date")

        if expiration_date and expiration_date <= datetime.date.today():
            raise OutdatedVaccineError(expiration_date)

        if "wearing_a_mask" in visitor and not visitor["wearing_a_mask"]:
            raise NotWearingMaskError()

        return f"Welcome to {self.name}"
