from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError

        if "expiration_date" in visitor["vaccine"]:
            expiration_date = visitor["vaccine"]["expiration_date"]
            if expiration_date < datetime.date.today():
                raise OutdatedVaccineError

        if "wearing_a_mask" in visitor and not visitor["wearing_a_mask"]:
            raise NotWearingMaskError

        return f"Welcome to {self.name}"

