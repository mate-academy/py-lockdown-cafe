"""
This module holds Cafe class. If you are using PyCharm, it will tell you
that 'Cafe' is an imported foreign expression,which originally has a diacritic.
Consider using Café. But, if I change Cafe to Café,
I get a Typo: In word 'Café.
So,
just for the sake of being naughty,
I declare that module holds Café class :D
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
            raise NotWearingMaskError("Everyone has to wear "
                                      "masks in order to enter the premises")

        if "vaccine" not in visitor:
            raise NotVaccinatedError("Everyone has to "
                                     "be vaccinated to enter the premises")

        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Every vaccination "
                                       "has to be up-to-date")
        return f"Welcome to {self.name}"
