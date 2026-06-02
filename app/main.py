import datetime


class NotVaccinatedError(Exception):
    pass

class OutdatedVaccineError(Exception):
    pass


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        try:
            visitor["vaccine"]
        except KeyError:
            raise NotVaccinatedError
        ex_date = visitor["vaccine"]["expiration_date"]
        if ex_date < datetime.date.today():
            raise OutdatedVaccineError
