import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        visitor_name = visitor["name"]
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor_name} doesn't have vaccine")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor_name} "
                                       f"vaccine is outdated")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor_name} doesn't have mask")
        return f"Welcome to {self.name}"
