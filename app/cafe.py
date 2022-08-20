import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:

    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        today = datetime.date.today()
        visitor_keys = [i for i in visitor.keys()]
        if "vaccine" not in visitor_keys:
            raise NotVaccinatedError
        if visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError
        return f"Welcome to {self.name}"
