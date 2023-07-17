import datetime


class NotVaccinatedError(ValueError):
    pass


class OutdatedVaccineError(ValueError):
    pass


class NotWearingMaskError(ValueError):
    pass


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        if visitor["vaccine"]["expiration_date"] < (datetime.date.today() - datetime.timedelta(days=365)):
            raise OutdatedVaccineError
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError
        return f"Welcome to {self.name}"


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    count_not_wearing_mask = 0
    for index, visitor in enumerate(friends):
        try:
            cafe.visit_cafe(visitor)
        except NotVaccinatedError:
            return "All friends should be vaccinated"
        except OutdatedVaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_not_wearing_mask += 1
    if count_not_wearing_mask:
        return f"Friends should buy {count_not_wearing_mask} masks"
    return f"Friends can go to {cafe.name}"


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
yyy = go_to_cafe(friends, Cafe("KFC"))# == "Friends should buy 2 masks"
ttt = 0
