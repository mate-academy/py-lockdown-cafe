from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    mask_count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_count += 1
        if mask_count > 0 and friend is friends[-1]:
            return f"Friends should buy {mask_count} masks"
    return f"Friends can go to {cafe.name}"
