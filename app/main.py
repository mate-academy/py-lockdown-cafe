from app import errors
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    can_go_to_cafe = True
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except errors.VaccineError:
            can_go_to_cafe = False
            return "All friends should be vaccinated"
        except errors.NotWearingMaskError:
            can_go_to_cafe = False
            masks_to_buy += 1

    if can_go_to_cafe:
        return f"Friends can go to {cafe.name}"
    return f"Friends should buy {masks_to_buy} masks"
