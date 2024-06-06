import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = datetime.date.today()
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(f"{visitor["name"]} is not vaccinated.")
        elif today > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError(f"{visitor["name"]}"
                                       f" has expired vaccine.")
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"{visitor["name"]} must wear masks.")
        else:
            return f"Welcome to {self.name}"
