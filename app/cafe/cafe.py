from datetime import datetime


from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        visitor_name = visitor["name"]
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor_name} has no vaccine")

        if visitor["vaccine"]["expiration_date"] < datetime.now().date():
            raise OutdatedVaccineError(
                f"{visitor_name}'s vaccine certificate has expired"
            )

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor_name} should wear a mask")

        return f"Welcome to {self.name}"
