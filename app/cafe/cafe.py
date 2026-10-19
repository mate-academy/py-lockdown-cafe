import datetime


from app.errors import errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise errors.NotVaccinatedError("Visitor does not have a vaccine")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise errors.OutdatedVaccineError("Your vaccine expired!")
        if "wearing_a_mask" not in visitor or not visitor["wearing_a_mask"] :
            raise errors.NotWearingMaskError("You must wear a mask!")
        return f"Welcome to {self.name}"
