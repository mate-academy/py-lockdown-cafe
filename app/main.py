from .cafe import Cafe
from .errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    vaccinated_friends = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            vaccinated_friends += 1
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            if not friend["wearing_a_mask"]:
                masks_to_buy += 1
    if vaccinated_friends == len(friends):
        return f"Friends can go to {cafe.name}"
    else:
        return f"Friends should buy {masks_to_buy} masks"
