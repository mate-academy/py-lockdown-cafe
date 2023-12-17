import datetime
import errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise errors.NotVaccinatedError()
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise errors.OutdatedVaccineError()
        if not visitor["wearing_a_mask"]:
            raise errors.NotWearingMaskError()
        return f"Welcome to {self.name}"
