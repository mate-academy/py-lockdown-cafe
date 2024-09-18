import datetime
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        try:
            vaccine_key = visitor["vaccine"]
            vaccine_lifetime = vaccine_key["expiration_date"]
            current_datatime = datetime.date
            visitor_mask = visitor["wearing_a_mask"]
            if not vaccine_key:
                raise NotVaccinatedError
            if vaccine_lifetime < current_datatime:
                raise OutdatedVaccineError
            if not visitor_mask:
                raise NotWearingMaskError
        except Exception as e:
            pass

        else:
            return f"Welcome to {self.name}"
