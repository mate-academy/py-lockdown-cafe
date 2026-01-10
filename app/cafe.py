import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        date_today = datetime.date.today()
        wearing_a_mask = visitor["wearing_a_mask"]
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        elif date_today > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError
        elif "wearing_a_mask" not in visitor or wearing_a_mask is not True:
            raise NotWearingMaskError
        else:
            return f"Welcome to {self.name}"
