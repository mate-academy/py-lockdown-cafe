import datetime


from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        if not vaccine:
            raise NotVaccinatedError("visitor has no vaccine")
        expiration = vaccine.get("expiration_date")
        if expiration is not None and expiration < datetime.date.today():
            raise OutdatedVaccineError("vaccine expired")
        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("visitor does not wear a mask")
        return f"Welcome to {self.name}"
