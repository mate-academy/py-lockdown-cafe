import datetime
import app.errors as errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise errors.NotVaccinatedError(
                "NotVaccinatedError should be raised with a message"
            )
        if visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise errors.OutdatedVaccineError(
                "OutdatedVaccineError should be raised with a message"
            )
        if not visitor.get("wearing_a_mask"):
            raise errors.NotWearingMaskError(
                "NotWearingMaskError should be raised with a message"
            )
        return f"Welcome to {self.name}"
