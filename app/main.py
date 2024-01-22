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

    def visit_cafe(self, visitors: dict) -> str:
        if not visitors.get("vaccine"):
            raise NotVaccinatedError
        if visitors["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError
        if not visitors.get("wearing_a_mask"):
            raise NotWearingMaskError
        return (
            f"Welcome to {self.name}"
        )


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    without_mask = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except (NotVaccinatedError, OutdatedVaccineError):
            return (
                "All friends should be vaccinated"
            )
        except NotWearingMaskError:
            without_mask += 1
    if without_mask != 0:
        return (
            f"Friends should buy {without_mask} masks"
        )
    else:
        return (
            f"Friends can go to {cafe.name}"
        )


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