import datetime
from app.errors import NotVaccinatedError, OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "You have to be vaccinated. "
                "Please make a new vaccination!")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "The date of your vaccine has expired. "
                "Please, make a new vaccination"
            )
        elif (
                "wearing_a_mask" not in visitor
                or visitor["wearing_a_mask"] is False
        ):
            raise NotWearingMaskError("To enter you should wear a mask!")
        return f"Welcome to {self.name}"
