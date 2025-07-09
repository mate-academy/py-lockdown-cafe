import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        rules_broken = 0
        if not visitor.get("vaccine"):
            rules_broken += 1
            raise NotVaccinatedError()
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            rules_broken += 1
            raise OutdatedVaccineError()
        if not visitor.get("wearing_a_mask"):
            rules_broken += 1
            raise NotWearingMaskError()
        if rules_broken == 0:
            return f"Welcome to {self.name}"
