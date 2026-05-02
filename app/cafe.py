import datetime


from app.errors import OutdatedVaccineError, NotWearingMaskError, \
    NotVaccinatedError


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f'{visitor["name"]} is not vaccinated')
        vaccine_dict = visitor["vaccine"]
        if vaccine_dict["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f'{visitor["name"]} vaccine is expired')
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(f'{visitor["name"]} not wearing a mask')
        else:
            return f"Welcome to {self.name}"
