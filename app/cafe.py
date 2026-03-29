from datetime import date

from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not ("vaccine" in visitor):
            raise NotVaccinatedError("The visitor does "
                                     "not have a vaccine")
        if not ("expiration_date" in visitor["vaccine"]) or \
                visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("The vaccine "
                                       "has expired")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("The visitor is "
                                      "not wearing a mask")

        return f"Welcome to {self.name}"
