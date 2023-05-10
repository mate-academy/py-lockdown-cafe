import datetime


class VaccineError(Exception):
    """Parent class"""


class NotVaccinatedError(VaccineError):
    """Visitor does not have a vaccine."""


class OutdatedVaccineError(VaccineError):
    """The vaccine must not be expired"""


class NotWearingMaskError(Exception):
    """All visitors must wear masks"""


class Cafe():
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):  # visitor["vaccine"]
        if "vaccine" not in visitor.keys():
            print(';(')  # TODO: delete print
            raise NotVaccinatedError("Visitor does not have a vaccine.")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The vaccine must not be expired.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("All visitors must wear masks.")
        print(f"Welcome to {self.name}")  # TODO: delete print
        return f"Welcome to {self.name}"


def go_to_cafe(friends: list, cafe):
    mask_to_buy = False
    for person in friends:
        try:
            print(person)  # TODO: delete print
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"

        except NotWearingMaskError:
            mask_to_buy += 1
    if mask_to_buy is not False:
        print(f"Friends should buy {mask_to_buy} masks")  # TODO: delete print
        return f"Friends should buy {mask_to_buy} masks"

    print(f"Friends can go to {cafe.name}")  # TODO: delete print
    return f"Friends can go to {cafe.name}"


friends = [
    {
        "name": "Alisa",
        "wearing_a_mask": True
    },
    {
        "name": "Bob",
        "vaccine": {
            "expiration_date": datetime.date.today()
        },
        "wearing_a_mask": True
    },
]
print(go_to_cafe(friends, Cafe("KFC")))
