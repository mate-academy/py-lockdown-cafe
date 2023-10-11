import datetime
import app.errors as errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if ("vaccine" not in visitor):
            raise errors.NotVaccinatedError
        if (datetime.date.today() > visitor["vaccine"]["expiration_date"]):
            raise errors.OutdatedVaccineError
        if (("wearing_a_mask" not in visitor) or (not visitor["wearing_a_mask"])):
            raise errors.NotWearingMaskError

        return f"Welcome to {self.name}"
