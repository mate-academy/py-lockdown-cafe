import datetime

from app.errors import NotVaccinatedError
from app.errors import NotWearingMaskError
from app.errors import OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("You must be vaccinated")
        else:
            date_now = datetime.datetime.now()
            if visitor["vaccine"]["expiration_date"] < date_now.date():
                raise OutdatedVaccineError("You must be vaccinated")
            else:
                if not visitor["wearing_a_mask"]:
                    raise NotWearingMaskError("You must be in a wearing mask")
                else:
                    return f"Welcome to {self.name}"
