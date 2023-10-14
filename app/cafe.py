import datetime

import app.errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine"):
            expiration_date = visitor.get("vaccine").get("expiration_date")
        else:
            raise app.errors.NotVaccinatedError("")
        if expiration_date < datetime.date.today():
            raise app.errors.OutdatedVaccineError
        if not visitor.get("wearing_a_mask"):
            raise app.errors.NotWearingMaskError

        return f"Welcome to {self.name}"
