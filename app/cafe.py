import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError
        else:
            if (visitor["vaccine"]["expiration_date"]
                    < datetime.date.today()):
                raise OutdatedVaccineError
        if (visitor.get("wearing_a_mask") is None
                or not visitor["wearing_a_mask"]):
            raise NotWearingMaskError
        else:
            return f"Welcome to {self.name}"
