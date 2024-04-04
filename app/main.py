from app.cafe import Cafe
from app.errors import *


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    mask = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)

        except VaccineError:
            return f"All friends should be vaccinated"
        except NotWearingMaskError:
            mask += 1

    if mask:
        return f"Friends should by {mask} masks"

    return "Friends can go to {cafe.name}"





