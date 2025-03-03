import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError
                        )


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        got_vaccine = visitor.get("vaccine")
        exp_date = got_vaccine.get("expiration_date") if got_vaccine else None
        has_mask = visitor.get("wearing_a_mask")

        if not got_vaccine:
            raise (NotVaccinatedError
                   ("All visitors should be vaccinated"))
        if got_vaccine and exp_date < datetime.date.today():
            raise (OutdatedVaccineError
                   ("The vaccine expiration date has passed."))
        if not has_mask:
            raise (NotWearingMaskError
                   ("All visitors should wear a mask"))
        return f"Welcome to {self.name}"
