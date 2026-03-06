import errors
import datetime


class Cafe():
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if "vaccine" not in visitor.keys():
            raise errors.NotVaccinatedError
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise errors.OutdatedVaccineError
        elif not visitor["wearing_a_mask"]:
            raise errors.NotWearingMaskError
        else:
            return f"Welcome to {self.name}"