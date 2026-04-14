import datetime

import app.errors as error


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine_info = visitor.get("vaccine", False)
        expiration_date = None
        if vaccine_info:
            expiration_date = vaccine_info.get("expiration_date")
        is_wearing_mask = visitor.get("wearing_a_mask", False)

        if not vaccine_info:
            raise error.NotVaccinatedError(
                "Visitor is not vaccinated."
            )
        if not expiration_date or expiration_date < datetime.date.today():
            raise error.OutdatedVaccineError(
                "Visitor's vaccine expired on {expiration_date}."
            )
        if not is_wearing_mask:
            raise error.NotWearingMaskError(
                "Friend should buy a mask"
            )

        return f"Welcome to {self.name}"
