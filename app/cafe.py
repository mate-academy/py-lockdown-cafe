import datetime
from app.errors import NotVaccinatedError,\
    OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            if "vaccine" not in visitor:
                raise NotVaccinatedError("Visitor must be vaccinated")
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("Visitor must have expired vaccine")
            if not visitor["wearing_a_mask"]:
                raise NotWearingMaskError("Visitor must have a mask")
        except (NotVaccinatedError,
                OutdatedVaccineError, NotWearingMaskError) as e:
            raise e
        else:
            return f"Welcome to {self.name}"
