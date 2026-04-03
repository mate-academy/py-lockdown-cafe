from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    humans_without_mask = 0
    for human in friends:
        try:
            cafe.visit_cafe(human)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            humans_without_mask += 1

    if humans_without_mask:
        return f"Friends should buy {humans_without_mask} masks"
    return f"Friends can go to {cafe.name}"
