from datetime import datetime
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("There is no vaccine!")

        expiration_date = visitor["vaccine"].get("expiration_date")
        if isinstance(expiration_date, str):
            expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d").date()

        if expiration_date < datetime.today().date():
            raise OutdatedVaccineError("The vaccine has expired!")

        if not visitor.get("mask", False):
            raise NotWearingMaskError(f"{visitor["name"]} is not wearing a mask!")

        return f"Welcome to {self.name}"

