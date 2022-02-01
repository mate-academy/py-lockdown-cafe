"""
This module holds Cafe class. If you are using PyCharm, it will tell you
that 'Cafe' is an imported foreign expression,which originally has a diacritic.
Consider using café. But, if I change Cafe to café,
I get a Typo: In word 'café.
So,
just for the sake of being naughty,
I declare that module holds café class :D
P.S. I wish I could change tests for this case
"""


from datetime import date
from app.errors import NotWearingMaskError, \
    NotVaccinatedError, OutdatedVaccineError


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor):
        """
        Just checking if a visitor is café-worthy
        """
        if not visitor["wearing_a_mask"]:
            print("No mask -> virus gets in -> die")
            raise NotWearingMaskError

        if "vaccine" not in visitor:
            print("No vaccine -> virus gets in -> die")
            raise NotVaccinatedError

        if visitor["vaccine"]["expiration_date"] < date.today():
            print("Outdated vaccine -> virus gets in -> die")
            raise OutdatedVaccineError

        return f"Welcome to {self.name}"
