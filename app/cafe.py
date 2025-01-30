import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe():
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        current_date = datetime.date.today()
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("NotVaccinatedError")
        else :
            expiration_date = visitor.get("vaccine").get("expiration_date")
            if expiration_date < current_date:
                raise OutdatedVaccineError("OutdatedVaccineError")
            elif "wearing_a_mask" in visitor and not visitor["wearing_a_mask"]:
                raise NotWearingMaskError("NotWearingMaskError")

        return f"Welcome to {self.name}"
