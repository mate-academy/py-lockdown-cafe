import datetime

from app.errors import NotWearingMaskError

from app.errors import OutdatedVaccineError

from app.errors import NotVaccinatedError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} don`t vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise (
                OutdatedVaccineError
                (f"{visitor['name']} vaccination outdated")
            )
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"{visitor['name']} don`t wear mask")
        return f"Welcome to {self.name}"
