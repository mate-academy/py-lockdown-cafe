from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    man_without_mask = 0

    for Friend in friends:
        try:
            cafe.visit_cafe(Friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            man_without_mask += 1
    if not man_without_mask:
        return f"Friends can go to {cafe.name}"
    return f"Friends should buy {man_without_mask} masks"
