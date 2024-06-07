import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not ("vaccine" in visitor):
            raise NotVaccinatedError("You must enter a vaccine.")

        vcc_expiration_date = visitor["vaccine"]["expiration_date"]
        current_date = datetime.date.today()

        if not vcc_expiration_date > current_date:
            raise OutdatedVaccineError

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
