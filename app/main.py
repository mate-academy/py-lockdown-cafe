from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    do_not_have_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            do_not_have_mask += 1

    if do_not_have_mask:
        return f"Friends should buy {do_not_have_mask} masks"
    return f"Friends can go to {cafe.name}"
