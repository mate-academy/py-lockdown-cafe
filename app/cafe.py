from datetime import date


from app.errors import NotVaccinatedError, \
    NotWearingMaskError, OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Vaccine has expired")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor doesn't wear the mask")
        return f"Welcome to {self.name}"
