import datetime
from app import errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor:
            raise errors.NotVaccinatedError("All friends should be vaccinated")
        else:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise (errors.OutdatedVaccineError
                       ("All friends should be vaccinated"))
            elif ("wearing_a_mask" not in visitor
                  or not visitor["wearing_a_mask"]):
                raise errors.NotWearingMaskError("Friends should buy masks")
            return f"Welcome to {self.name}"
