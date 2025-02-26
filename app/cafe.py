from datetime import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        from app.errors import NotVaccinatedError, OutdatedVaccineError, \
            NotWearingMaskError

        if not visitor.get("vaccine"):
            raise NotVaccinatedError()

        if visitor["vaccine"]["expiration_date"] < datetime.today().date():
            raise OutdatedVaccineError()

        if (not visitor.get("wearing_a_mask")
                or visitor["wearing_a_mask"] is False):
            raise NotWearingMaskError()

        return f"Welcome to {self.name}"
