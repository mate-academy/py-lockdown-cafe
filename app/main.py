import datetime

test_visitor = {
    "name": "Paul",
    "age": 23,
    "vaccine": {
        "expiration_date": datetime.date(2022, 2, 23)
        },
    "wearing_a_mask": True

}


test_visitor_NON = {
    "name": "Ivan",
}


class NotVaccinatedError(Exception):
    def __init__(self, text: str = "NotVaccinatedError") -> None:
        print(text)


class OutdatedVaccineError(Exception):
    def __init__(self, text: str = "OutdatedVaccineError") -> None:
        print(text)


class NotWearingMaskError(Exception):
    def __init__(self, text: str = "NotWearingMaskError") -> None:
        print(text)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict):
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("NotWearingMaskError")

        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError")

        vaccine_date = visitor["vaccine"]["expiration_date"]
        if vaccine_date < datetime.date.today():
            raise OutdatedVaccineError("OutdatedVaccineError")
        return f"Welcome to {self.name}"


kfc = Cafe("KFC")
kfc.visit_cafe(test_visitor)

