from app.errors import VaccineError
from app.errors import NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: "Cafe") -> str:
    mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask += 1
    if mask:
        return f"Friends should buy {mask} masks"
    return f"Friends can go to {cafe.name}"
