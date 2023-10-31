import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        visitor_name = visitor.get("name")
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError(f"{visitor_name} "
                                     f"should vaccine to visit this cafe")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor_name}'s "
                                       f"vaccine is expired")
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"{visitor_name} "
                                      f"should wear mask to visit this cafe")
        else:
            return f"Welcome to {self.name}"
