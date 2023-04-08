import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("Visitor does not have a vaccine key")

        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "You have an expired vaccine. You can't visit the cafe"
            )
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Not all visitors have a mask")
        return f"Welcome to {self.name}"
