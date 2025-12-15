import datetime
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError, OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | Exception:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You need vaccine to visit this cafe")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("You need to renew your vaccine")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("You need to wear a mask")
        else:
            return f"Welcome to {self.name}"
