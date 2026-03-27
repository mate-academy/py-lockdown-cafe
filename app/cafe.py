"""
This cafe.py module contains a constructor
for cafe instances. Besides the name of cafe,
class contains particular method to check any
visitor, before he can enter a cafe. This method
checks a vaccine (and it`s expiration date) and
a mask - every visitor must wear the mask to visit
cafe.
"""


import datetime
from app.errors import NotVaccinatedError, \
    NotWearingMaskError, \
    OutdatedVaccineError


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("Visitor must be vaccinated.")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine has been expired.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor must wear a mask to visit cafe.")

        return f"Welcome to {self.name}"
