from app.cafe import Cafe, date
from app.errors import \
    NotVaccinatedError, \
    OutdatedVaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    is_vaccinated = True

    for idx, friend in enumerate(friends):
        try:
            if "vaccine" not in friend:
                is_vaccinated = False
                break

            if friend["vaccine"]["expiration_date"] < date.today():
                is_vaccinated = False
                break

            if not friend.get("wearing_a_mask", True):
                masks_to_buy += 1

        except (KeyError, NotVaccinatedError, OutdatedVaccineError):
            is_vaccinated = False
            break

    if not is_vaccinated:
        return "All friends should be vaccinated"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"


if __name__ == "__main__":
    kfc = Cafe("KFC")

    visitor = {
        "name": "Paul",
        "age": 23,
        "vaccine": {
            "expiration_date": date.today()
        },
        "wearing_a_mask": True
    }

    print(kfc.visit_cafe(visitor))  # Welcome to KFC

    friends = [
        {
            "name": "Alisa",
            "vaccine": {
                "expiration_date": date.today()
            },
            "wearing_a_mask": True
        },
        {
            "name": "Bob",
            "vaccine": {
                "expiration_date": date.today()
            },
            "wearing_a_mask": True
        },
    ]

    print(go_to_cafe(friends, kfc))  # Friends can go to KFC

    friends = [
        {
            "name": "Alisa",
            "vaccine": {
                "expiration_date": date.today()
            },
            "wearing_a_mask": False
        },
        {
            "name": "Bob",
            "vaccine": {
                "expiration_date": date.today()
            },
            "wearing_a_mask": False
        },
    ]

    print(go_to_cafe(friends, kfc))  # Friends should buy 2 masks
