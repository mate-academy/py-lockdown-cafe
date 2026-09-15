import datetime


from app.errors import OutdatedVaccineError
from app.errors import NotVaccinatedError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} have not a vaccine")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor['name']}"
                                       f" have outdated vaccine")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(f"{visitor['name']} should wear a mask")
        else:
            return f"Welcome to {self.name}"
