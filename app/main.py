import datetime


class NotVaccinatedError(Exception):
    pass


class OutdatedVaccineError(Exception):
    pass


class NotWearingMaskError(Exception):
    pass


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError")
        else:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("OutDatedVaccineError")
            else:
                if "wearing_a_mask" not in visitor or not visitor["wearing_a_mask"]:
                    raise NotWearingMaskError("NotWearingMaskError")
                else:
                    return f"Wellcome to {self.name}"


kfc = Cafe("KFC")
visitor = {
    "name": "Paul",
    "age": 23,
    "vaccine": {"expiration_date": datetime.date.today()},
}
try:
    print(kfc.visit_cafe(visitor))
except Exception as e:
    print(e)
