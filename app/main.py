from app.cafe import Cafe
from app.errors import (NotVaccinatedError, OutdatedVaccineError,
                        NotWearingMaskError)
import datetime


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_needed = 0
    all_vaccinated = True

    for friend in friends:
        try:
            if "vaccine" not in friend:
                all_vaccinated = False
                continue

            expiration_date = friend["vaccine"]["expiration_date"]
            if expiration_date < datetime.date.today():
                all_vaccinated = False

            if not friend.get("wearing_a_mask", False):
                masks_needed += 1

        except NotVaccinatedError:
            all_vaccinated = False
        except OutdatedVaccineError:
            all_vaccinated = False
        except NotWearingMaskError:
            masks_needed += 1

    if not all_vaccinated:
        return "All friends should be vaccinated"

    if masks_needed > 0:
        return f"Friends should buy {masks_needed} masks"

    return f"Friends can go to {cafe.name}"


# Example usage
if __name__ == "__main__":
    kfc = Cafe("KFC")

    friends = [
        {
            "name": "Alisa",
            "vaccine": {
                "expiration_date": datetime.date.today()
            },
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

    print(go_to_cafe(friends, kfc))

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

    print(go_to_cafe(friends, kfc))

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

    print(go_to_cafe(friends, kfc))
