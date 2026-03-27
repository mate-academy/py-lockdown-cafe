from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe():
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vis_name = visitor["name"]
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"No Vaccine : {vis_name} !")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(f"Outdated Vaccine : {vis_name} !")
        if ("wearing_a_mask" not in visitor
                or not visitor["wearing_a_mask"]):
            raise NotWearingMaskError(f"No Mask : {vis_name} !")
        return f"Welcome to {self.name}"
