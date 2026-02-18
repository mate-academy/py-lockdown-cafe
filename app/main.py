from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    maskless_count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            maskless_count += 1
    if maskless_count == 0:
        return f"Friends can go to {cafe.name}"
    else:
        return f"Friends should buy {maskless_count} masks"
