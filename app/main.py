from app.cafe import Cafe

from app.errors import VaccineError
from app.errors import NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    no_mask = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            no_mask += 1

    if no_mask == 0:
        return f"Friends can go to {cafe.name}"
    return f"Friends should buy {no_mask} masks"
