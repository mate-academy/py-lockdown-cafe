from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)
import datetime


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor.keys():
            """All friends should be vaccinated"""
            raise NotVaccinatedError
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            """The vaccine should be with the normal term"""
            raise OutdatedVaccineError
        if visitor["wearing_a_mask"] is False:
            """All guests must wear masks"""
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
