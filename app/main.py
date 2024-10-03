
from app.errors import (
    NotWearingMaskError,
    VaccineError
)
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> VaccineError | str:
    have_not_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            have_not_mask += 1
    if have_not_mask:
        return f"Friends should buy {have_not_mask} masks"
    return f"Friends can go to {cafe.name}"


if __name__ == "__main__":
    import datetime
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
    print(go_to_cafe(friends, Cafe("KFC")))
