import datetime
from app.errors import NotVaccinatedError
from app.errors import NotWearingMaskError
from app.errors import OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if "vaccine" not in visitor:
            try:
                raise NotVaccinatedError
            except NotVaccinatedError:
                raise

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            try:
                raise OutdatedVaccineError
            except OutdatedVaccineError:
                raise

        if not visitor["wearing_a_mask"]:
            try:
                raise NotWearingMaskError
            except NotWearingMaskError:
                raise

        return f"Welcome to {self.name}"
