import datetime
from typing import Union
from app.errors import NotVaccinatedError
from app.errors import NotWearingMaskError
from app.errors import OutdatedVaccineError


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Union[str, Exception]:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All friends should be vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("All friends should have actual "
                                       "vaccination certificate")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Friends should buy masks")
        return f"Welcome to {self.name}"
