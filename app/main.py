from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError
import datetime


def sorted_friends(friend: dict) -> int:
    """I don't know how else to solve this task without using this function,
    I tried for two days"""

    return (
        0 if not friend.get("vaccine")
        or friend["vaccine"]["expiration_date"] < datetime.date.today()
        else 1
    )


def go_to_cafe(friends: list, cafe: Cafe) -> str:

    count = sum([1 for person in friends if not person["wearing_a_mask"]])
    try:
        [cafe.visit_cafe(friend)
         for friend in sorted(friends, key=sorted_friends)]
    except VaccineError:
        return "All friends should be vaccinated"
    except NotWearingMaskError:
        return f"Friends should buy {count} masks"
    return f"Friends can go to {cafe.name}"
