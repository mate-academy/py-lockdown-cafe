import datetime
from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        data_today = datetime.date.today()

        if "vaccine" not in visitor:
            raise NotVaccinatedError(visitor["name"])

        if ("vaccine" in visitor
                and data_today > visitor["vaccine"]["expiration_date"]):
            print(f"Today's date: {data_today}")
            print(f"Vaccine expiration date: "
                  f"{visitor["vaccine"]["expiration_date"]}")
            raise OutdatedVaccineError(visitor["name"])

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(visitor["name"])

        return f"Welcome to {self.name}"
