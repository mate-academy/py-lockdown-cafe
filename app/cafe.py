import datetime

from . import errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not ("vaccine" in visitor.keys()):
            raise errors.NotVaccinatedError("You should be vaccinated")
        today = datetime.date.today()
        if visitor.get("vaccine").get("expiration_date") < today:
            raise errors.OutdatedVaccineError("Your vaccine is outdated")
        if not visitor.get("wearing_a_mask"):
            raise errors.NotWearingMaskError("You should wear a mask")
        return f"Welcome to {self.name}"
