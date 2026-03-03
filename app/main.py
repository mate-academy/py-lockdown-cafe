from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    counter = 0
    for friend in friends:
        try:
            cafe.visit_cafe(visitor=friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_to_buy = sum([1 for friend in friends
                               if friend.get("wearing_a_mask") is False])
            counter += 1
    if counter != 0:
        return f"Friends should buy {mask_to_buy} masks"
    return f"Friends can go to {cafe.name}"
