from datetime import date
from typing import Dict, Union
from errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self,
                   visitor:
                   Dict
                   [
                       str, Union[str, int, Dict[str, Union[date, None]], bool]
                   ]
                   ) \
            -> str:

        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        vaccine_exp_date = visitor["vaccine"].get("expiration_date")
        if vaccine_exp_date and vaccine_exp_date < date.today():
            raise OutdatedVaccineError("Vaccine is outdated")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
