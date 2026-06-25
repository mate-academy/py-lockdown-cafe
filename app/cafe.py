import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Error! The visitor doesn`t have vaccine")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Error! "
                                       "The visitor`s vaccine is outdated")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Error! The visitor doesn't wear a mask")
        return f"Welcome to {self.name}"
