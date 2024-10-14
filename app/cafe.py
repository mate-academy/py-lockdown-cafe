import datetime

from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if vaccine := visitor.get("vaccine"):
            if datetime.date.today() > vaccine.get("expiration_date"):
                raise OutdatedVaccineError
        else:
            raise NotVaccinatedError

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
