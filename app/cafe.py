import datetime
from app.errors import (
    OutdatedVaccineError,
    NotWearingMaskError,
    NotVaccinatedError
)


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            message = f'{visitor["name"]} doesn\'t have vaccine'
            raise NotVaccinatedError(message)

        today = datetime.date.today()
        expired_date = visitor["vaccine"]["expiration_date"]
        if expired_date < today:
            days = today - expired_date
            message = (f'{visitor["name"]} vaccine has expired {days} '
                       f'days ago and he should take a new')
            raise OutdatedVaccineError(message)

        if not visitor["wearing_a_mask"]:
            message = f'{visitor["name"]} doesn\'t wear mask'
            raise NotWearingMaskError(message)
        return f"Welcome to {self.name}"
