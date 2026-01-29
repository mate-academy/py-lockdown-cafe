import datetime

from app.errors import (OutdatedVaccineError, NotVaccinatedError,
                        NotWearingMaskError)


class Cafe:
    def __init__(
            self,
            name: str
    ) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        current_time = datetime.date.today()
        if not visitor.get("vaccine"):
            raise NotVaccinatedError
        elif current_time > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError
        return f"Welcome to {self.name}"
