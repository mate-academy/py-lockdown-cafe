import datetime

import app.errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise app.errors.NotVaccinatedError("No vaccine certificate.")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise app.errors.OutdatedVaccineError("Certificate is outdated.")
        if visitor["wearing_a_mask"] is not True:
            raise app.errors.NotWearingMaskError("Visitor without mask.")
        return f"Welcome to {self.name}"
