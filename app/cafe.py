import datetime


from app.errors import NotVaccinatedError, NotWearingMaskError, OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict):
        self.visitor = visitor
        if not self.visitor.get("vaccine"):
            raise NotVaccinatedError("Friend should be vaccinated")
        if self.visitor.get("vaccine", {}).get("expiration_date"):
             if self.visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("The vaccine must not be expired")
        if not self.visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Friend should buy a mask")
        return f"Welcome to {self.name}"

