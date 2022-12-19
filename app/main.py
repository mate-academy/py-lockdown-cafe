import datetime


class VaccineError(Exception):

    def __str__(self):
        return "All friends should be vaccinated"


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    pass


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        masks_to_buy = 0
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError
        elif not visitor["wearing_a_mask"]:
            masks_to_buy += 1
            raise NotWearingMaskError(f"Friends should buy {masks_to_buy} masks")
        else:
            print(f"Welcome to {self.name}")


def go_to_cafe(friends: list, cafe: Cafe):
    num = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError as e:
            num += 1
            print(e)
        except NotWearingMaskError as e:
            num += 1
            print(e)
    if num == 0:
        print(f"Friends can go to {cafe.name}")


friends = [
    {
        "name": "Alisa",
        "vaccine": {
            "expiration_date": datetime.date.today()
        },
        "wearing_a_mask": False
    },
    {
        "name": "Bob",
        "vaccine": {
            "expiration_date": datetime.date.today()
        },
        "wearing_a_mask": False
    },
]
go_to_cafe(friends, Cafe("KFC"))

