from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name: str):
        self._name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        if "expiration_date" in visitor["vaccine"] and \
                visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError
        return f"Welcome to {self._name}"

    @property
    def name(self) -> str:
        return self._name
