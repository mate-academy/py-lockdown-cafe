from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
import datetime


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        visitor_name = visitor["name"]

        if "vaccine" not in visitor:
            raise NotVaccinatedError(visitor_name)

        if visitor["vaccine"].get("expiration_date",
                                  datetime.date.min
                                  ) < datetime.date.today():
            raise OutdatedVaccineError(visitor_name)

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(visitor_name)

        return f"Welcome to {self.name}"
