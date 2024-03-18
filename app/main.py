from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    no_mask = 0
    for human in friends:
        try:
            cafe.visit_cafe(human)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            no_mask += 1

    if no_mask:
        return f"Friends should buy {no_mask} masks"
    else:
        return f"Friends can go to {cafe.name}"
