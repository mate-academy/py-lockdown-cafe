import datetime


class NotVaccinatedError(Exception):
    pass


class OutdatedVaccineError(Exception):
    pass


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError")
        else:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("OutDatedVaccineError")


kfc = Cafe("KFC")
visitor = {
    "name": "Paul",
    "age": 23,
    "vaccine": {"expiration_date": datetime.date(year=2019, month=2, day=23)},
}
try:
    kfc.visit_cafe(visitor)
except Exception as e:
    print(e)
