from app import errors
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except errors.VaccineError:
            return "All friends should be vaccinated"
        except errors.NotWearingMaskError:
            pass

    masks_to_buy = 0

    for friend in friends:
        if not friend["wearing_a_mask"]:
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
