from app.errors import *
import datetime


class Cafe():
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("немає вакцини")
        elif "wearing_a_mask" in visitor.keys() and not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Без маски")
        else:
            dif_days = (datetime.date.today() - visitor["vaccine"]["expiration_date"]).days
            if dif_days > 180:
                raise OutdatedVaccineError(f"ВАКЦИНА ПРОСТРОЧЕНА, на {dif_days - 180} дні")
            print(f"Welcome to {self.name}")


if __name__ == "__main__":
    kfc = Cafe("KFC")
    visitor = {
        "name": "Paul",
        "age": 23,
        "vaccine": {
            "expiration_date": datetime.date.today()
        },
        "wearing_a_mask": True
    }
    kfc.visit_cafe(visitor)
