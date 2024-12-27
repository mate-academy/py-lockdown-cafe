import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            if not visitor["vaccine"]:
                raise NotVaccinatedError("NotVaccinatedError")
        except KeyError:
            raise NotVaccinatedError("NotVaccinatedError")
        try:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("OutdatedVaccineError")
            if visitor["wearing_a_mask"] is False:
                raise NotWearingMaskError("NotWearingMaskError")
        except KeyError as e:
            print(e)
        else:
            return f"Welcome to {self.name}"
