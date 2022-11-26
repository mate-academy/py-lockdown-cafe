from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(visitor=friend)
        except VaccineError:
            return "All friends should be vaccinated"

        except NotWearingMaskError:
            masks += 1
    if masks > 0:
        return f"Friends should buy {masks} masks"

    return f"Friends can go to {cafe.name}"
