import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("Need to vaccinate.")
        else:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("Need to vaccinate again.")
            elif (visitor.get("wearing_a_mask") is None
                  or visitor.get("wearing_a_mask") is False):
                raise NotWearingMaskError("Need to wear mask")
            else:
                return f"Welcome to {self.name}"
