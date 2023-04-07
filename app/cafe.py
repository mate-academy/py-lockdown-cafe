import datetime
from app.errors import NotVaccinatedError, NotWearingMaskError
from app.errors import OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not ("vaccine" in visitor):
            raise NotVaccinatedError(
                "The visitor is not vaccinated"
            )

        valid_until = visitor["vaccine"]
        if valid_until["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "The visitor has an overdue vaccine"
            )
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                "The visitor does not have a mask"
            )
        return f"Welcome to {self.name}"
