import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']}"
                                     f" is not vaccinated.")

        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date and expiration_date < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor['name']}'s"
                                       f" vaccine is expired")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(f"{visitor['name']}"
                                      f" is not wearing a mask")

        return f"Welcome to {self.name}"
