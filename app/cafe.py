import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError

        expiration_date = visitor["vaccine"].get("expiration_date")
        if (expiration_date is None
                or expiration_date < datetime.date.today()):
            raise OutdatedVaccineError

        visitor_wears_a_mask = visitor.get("wearing_a_mask")
        if (visitor_wears_a_mask is None) or (not visitor_wears_a_mask):
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
