import datetime

import app.errors as errors


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise errors.NotVaccinatedError("Visitor should have a vaccine")
        elif datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise errors.OutdatedVaccineError("Vaccine is outdated")
        elif not visitor["wearing_a_mask"]:
            raise errors.NotWearingMaskError("Visitor should wear a mask")

        return f"Welcome to {self.name}"
