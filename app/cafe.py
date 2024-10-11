import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "Visitor is not vaccinated. "
                "Vaccination is required to enter the cafe."
            )

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "Visitors vaccine is expired. "
                "A valid vaccine is required to enter the cafe."
            )

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                "Visitor did not wear a mask. "
                "It is very important to wear masks during lockdown"
            )

        return f"Welcome to {self.name}"
