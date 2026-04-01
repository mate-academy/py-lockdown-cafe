from datetime import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)
from app.models.visitor import Visitor


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Visitor) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        vaccine_expiration_date = (visitor
                                   .get("vaccine", {})
                                   .get("expiration_date"))

        if vaccine_expiration_date < datetime.now().date():
            raise OutdatedVaccineError("Visitors vaccine is outdated")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing the mask")

        return f"Welcome to {self.name}"
