from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    no_mask = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            no_mask += 1

    if no_mask > 0:
        return f"Friends should buy {no_mask} masks"

    return f"Friends can go to {cafe.name}"


if __name__ == "__main__":
    import datetime

    friends = [
        {
            "name": "Alisa",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True
        },
    ]

    print(go_to_cafe(friends, Cafe("KFC")))
