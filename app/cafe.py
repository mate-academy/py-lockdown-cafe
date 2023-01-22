import datetime


from app.errors import NotVaccinatedError
from app.errors import NotWearingMaskError
from app.errors import OutdatedVaccineError


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} must be vaccinated!")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine should be fresh!")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Always take masks with yourself!")

        return f"Welcome to {self.name}"
