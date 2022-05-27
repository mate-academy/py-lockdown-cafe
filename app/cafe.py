import datetime
from app.errors import (
    OutdatedVaccineError,
    NotWearingMaskError,
    NotVaccinatedError
)


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitors: dict):
        if "vaccine" not in visitors:
            message = f'{visitors["name"]} doesn\'t have vaccine'
            raise NotVaccinatedError(message)

        today = datetime.date.today()
        expired_date = visitors["vaccine"]["expiration_date"]

        if expired_date < today:
            days = today - expired_date
            message = (f'{visitors["name"]} vaccine has expired {days} '
                       f'days ago and she or he should take a new')
            raise OutdatedVaccineError(message)

        if not visitors["wearing_a_mask"]:
            message = f'{visitors["name"]} doesn\'t wear mask'
            raise NotWearingMaskError(message)

        return f"Welcome to {self.name}"
