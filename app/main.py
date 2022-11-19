import datetime


class NotVaccinatedError(Exception):
    pass


class OutdatedVaccineError(NotVaccinatedError):
    pass


class NotWearingMaskError(NotVaccinatedError):
    pass


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError
        elif not visitor["vaccine"]["expiration_date"]\
                >= datetime.date.today():
            raise OutdatedVaccineError
        return f"Welcome to {self.name}"


kfc = Cafe("KFC")
visitor = {
    "name": "Paul",
    "age": 23,
    "vaccine": {
        "expiration_date": datetime.date.today()
    },
    "wearing_a_mask": True
}
print(kfc.visit_cafe(visitor))
