import datetime

from app import errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise errors.NotVaccinatedError("Not vaccinated")
        vaccine_info = visitor.get("vaccine")
        expiration_date = vaccine_info.get("expiration_date")
        if expiration_date < datetime.date.today():
            raise errors.OutdatedVaccineError("Outdated vaccine")
        if not visitor.get("wearing_a_mask"):
            raise errors.NotWearingMaskError("Not Wearing Mask")
        return f"Welcome to {self.name}"
