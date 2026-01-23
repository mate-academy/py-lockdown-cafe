import datetime

from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "The date of your vaccine has expired. "
                "Please, make a new vaccination"
            )

        expiration_date = visitor["vaccine"]["expiration_date"]
        day_today = datetime.date.today()

        if expiration_date < day_today:
            raise OutdatedVaccineError(
                "The date of your vaccine has expired. "
                "Please, make a new vaccination")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("To enter you should wear a mask!")

        return f"Welcome to {self.name}"
