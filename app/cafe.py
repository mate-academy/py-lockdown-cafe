import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = datetime.date.today()
        let_in = True
        if "vaccine" not in visitor.keys():
            let_in = False
            raise NotVaccinatedError
        elif visitor["vaccine"]["expiration_date"] < today:
            let_in = False
            raise OutdatedVaccineError
        if visitor["wearing_a_mask"] is False:
            let_in = False
            raise NotWearingMaskError
        if let_in:
            return f"Welcome to {self.name}"
