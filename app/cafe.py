from app.errors import \
    NotVaccinatedError,\
    OutdatedVaccineError, \
    NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        counter = 0
        if "vaccine" not in visitor:
            raise \
                NotVaccinatedError("You don't have a vaccine, you can't enter")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            counter += 1
            raise OutdatedVaccineError("Your vaccine's term is good")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Everyone should wear masks!")
        if counter == 0:
            return f"Welcome to {self.name}"
