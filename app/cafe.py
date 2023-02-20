import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict, *args) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor.get('name')} has no vaccine")

        current_date = datetime.date.today()
        expiration_date = visitor.get("vaccine").get("expiration_date")

        if current_date > expiration_date:
            raise OutdatedVaccineError(f"{visitor.get('name')}, "
                                       f"your vaccine has been expired")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"{visitor.get('name')} "
                                      f"you have to wearing mask here")

        return f"Welcome to {self.name}"
