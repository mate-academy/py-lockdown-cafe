import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            if not visitor["vaccine"]:
                raise NotVaccinatedError("visitor is not vaccinated")
        except KeyError:
            raise NotVaccinatedError("visitor is not vaccinated")
        try:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("visitors vaccine is outdated")

            if visitor["wearing_a_mask"] is False:
                raise NotWearingMaskError("visitor should wear a mask")

        except KeyError as e:
            raise NotVaccinatedError(f"missing key: {e}")
        else:
            return f"Welcome to {self.name}"
