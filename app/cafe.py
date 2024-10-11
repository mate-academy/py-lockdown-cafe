import datetime


from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError

        if visitor.get("vaccine").get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError

        return f"Welcome to {self.name}"


# kfc = Cafe("KFC")
# visitor = {
#     "name": "Paul",
#     "age": 23,
# }
# kfc.visit_cafe(visitor)     # NotVaccinatedError

# kfc = Cafe("KFC")
# visitor = {
#     "name": "Paul",
#     "age": 23,
#     "vaccine": {
#         "expiration_date": datetime.date(year=2019, month=2, day=23)
#     }
# }
# kfc.visit_cafe(visitor)     # OutdatedVaccineError

# kfc = Cafe("KFC")
# visitor = {
#     "name": "Paul",
#     "age": 23,
#     "vaccine": {
#         "expiration_date": datetime.date.today()
#     },
#     "wearing_a_mask": False
# }
# kfc.visit_cafe(visitor)     # NotWearingMaskError

# kfc = Cafe("KFC")
# visitor = {
#     "name": "Paul",
#     "age": 23,
#     "vaccine": {
#         "expiration_date": datetime.date.today()
#     },
#     "wearing_a_mask": True
# }
# print(kfc.visit_cafe(visitor) == "Welcome to KFC")
