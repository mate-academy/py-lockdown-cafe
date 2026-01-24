import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not isinstance(visitor, dict):
            raise NotVaccinatedError("Visitor's data is incorrect")
        visitor_name = visitor.get("name")
        visitor_vaccine_dict = visitor.get("vaccine")

        if not visitor_vaccine_dict:
            raise NotVaccinatedError(f"Visitor {visitor_name} "
                                     f"has no vaccination record")

        vaccine_date = visitor_vaccine_dict.get("expiration_date")
        if (not isinstance(vaccine_date, datetime.date)
                or vaccine_date < datetime.date.today()):
            raise OutdatedVaccineError(f"The vaccination of {visitor_name} "
                                       f"is expired")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"Visitor {visitor_name} "
                                      f"without mask")

        return f"Welcome to {self.name}"
