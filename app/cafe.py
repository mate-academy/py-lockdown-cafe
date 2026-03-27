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
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor.get('name')} has no vaccine")

        if (
                datetime.date.today()
                > visitor.get("vaccine").get("expiration_date")
        ):
            raise OutdatedVaccineError(f"{visitor.get('name')}, "
                                       f"your vaccine has been expired")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"{visitor.get('name')} "
                                      f"you have to wearing mask here")

        return f"Welcome to {self.name}"
