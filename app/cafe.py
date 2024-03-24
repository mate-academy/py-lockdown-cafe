import datetime

import app.errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        name = visitor["name"]
        if "vaccine" not in visitor:
            raise \
                app.errors.NotVaccinatedError(f"{name} is not vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise \
                app.errors.OutdatedVaccineError(f"{name} has expired vaccine")
        if visitor["wearing_a_mask"] is False:
            raise \
                app.errors.NotWearingMaskError(f"{name} doesn't wear mask")
        return f"Welcome to {self.name}"
