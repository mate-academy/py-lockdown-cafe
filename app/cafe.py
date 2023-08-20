import datetime
import app.errors as errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise errors.NotVaccinatedError(str(errors.NotVaccinatedError))
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise errors.OutdatedVaccineError(str(errors.OutdatedVaccineError))
        elif not visitor.get("wearing_a_mask", True):
            raise errors.NotWearingMaskError(str(errors.NotWearingMaskError))
        else:
            return f"Welcome to {self.name}"
