import datetime
from app.errors import (NotVaccinatedError,
                        NotWearingMaskError, OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitors: dict) -> str:
        flag = True
        if "vaccine" not in visitors.keys():
            flag = False
            raise NotVaccinatedError
        today = datetime.date.today()
        expiration_date = visitors["vaccine"]["expiration_date"]
        if expiration_date < today:
            flag = False
            raise OutdatedVaccineError
        mask = visitors.get("wearing_a_mask")
        if not mask:
            flag = False
            raise NotWearingMaskError
        if flag:
            return f"Welcome to {self.name}"
