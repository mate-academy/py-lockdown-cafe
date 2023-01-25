from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError
import datetime


def sorted_friends(friend: dict) -> int:
    return 0 if not friend.get("vaccine", False) or \
        friend["vaccine"]["expiration_date"] < datetime.date.today() else 1


def count_mask(persons: list) -> int:
    return sum([1 for person in persons if not person["wearing_a_mask"]])


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    try:
        [cafe.visit_cafe(friend)
         for friend in sorted(friends, key=sorted_friends)]
    except VaccineError:
        return "All friends should be vaccinated"
    except NotWearingMaskError:
        return f"Friends should buy {count_mask(friends)} masks"
    else:
        return f"Friends can go to {cafe.name}"
