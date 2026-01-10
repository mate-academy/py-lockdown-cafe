import datetime

from app.errors import (NotVaccinatedError, OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        date_today = datetime.date.today()

        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor is not vaccinated")
        elif date_today > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("The vaccine "
                                       "is outdated")
        elif ("wearing_a_mask" not in visitor
              or visitor["wearing_a_mask"] is not True):
            raise NotWearingMaskError("The visitor is not wearing a mask")
        else:
            return f"Welcome to {self.name}"
