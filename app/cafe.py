import datetime
from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You need to vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Your vaccine is out to date")
        if "wearing_a_mask" not in visitor:
            raise NotWearingMaskError("You need to wearing mask")
        else:
            if visitor["wearing_a_mask"] is not True:
                raise NotWearingMaskError("You need to wearing mask")
        return f"Welcome to {self.name}"
