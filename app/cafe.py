import datetime
from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine"):
            if visitor["vaccine"]["expiration_date"] >= datetime.date.today():
                if not visitor.get("wearing_a_mask"):
                    raise NotWearingMaskError(
                        "The visitor should have a mask!"
                    )
            else:
                raise OutdatedVaccineError(
                    "The visitor should get a new dose of vaccine!"
                )
        else:
            raise NotVaccinatedError(
                "The visitor should get vaccinated!"
            )
        return f"Welcome to {self.name}"
