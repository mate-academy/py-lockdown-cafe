from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You is not vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("""The vaccine has expired,
                                       you must be vaccinated""")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("""The visitor entered
                                    the cafe without a mask""")

        return f"Welcome to {self.name}"
