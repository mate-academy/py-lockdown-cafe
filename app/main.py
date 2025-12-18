import datetime
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    """Determines if a group of friends can visit the cafe."""
    masks_needed = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_needed += 1

    if masks_needed > 0:
        return f"Friends should buy {masks_needed} masks"

    return f"Friends can go to {cafe.name}"


# Example Usage:

if __name__ == "__main__":
    kfc = Cafe("KFC")

    friends1 = [
        {
            "name": "Alisa",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True,
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True,
        },
    ]
    print(go_to_cafe(friends1, kfc))  # "Friends can go to KFC"

    friends2 = [
        {
            "name": "Alisa",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": False,
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": False,
        },
    ]
    print(go_to_cafe(friends2, kfc))  # "Friends should buy 2 masks"

    friends3 = [
        {
            "name": "Alisa",
            "wearing_a_mask": True,
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True,
        },
    ]
    print(go_to_cafe(friends3, kfc))  # "All friends should be vaccinated"
