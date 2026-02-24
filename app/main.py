from typing import List
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: List, cafe: Cafe) -> str:
    friends_without_mask = 0

    for firend in friends:
        try:
            cafe.visit_cafe(firend)
        except (VaccineError):
            return "All friends should be vaccinated"
        except (NotWearingMaskError):
            friends_without_mask += 1

    if friends_without_mask != 0:
        return f"Friends should buy {friends_without_mask} masks"
    else:
        return f"Friends can go to {cafe.name}"
