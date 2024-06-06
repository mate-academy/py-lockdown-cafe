import datetime


class NotVaccinatedError(Exception):
    pass


class OutdatedVaccineError (Exception):
    pass


class NotWearingMaskError  (Exception):
    pass


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if not ("vaccine" in visitor):
            raise NotVaccinatedError

        vcc_expiration_date = visitor["vaccine"]["expiration_date"]
        current_date = datetime.date.today()

        if not vcc_expiration_date >= current_date:
            raise OutdatedVaccineError

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError


if __name__ == "__main__":
    kfc = Cafe("KFC")
    visitor = {
        "name": "Paul",
        "age": 23,
        "vaccine": {
            "expiration_date": datetime.date.today()
        },
        "wearing_a_mask": False
    }
    kfc.visit_cafe(visitor)  # NotWearingMaskError
