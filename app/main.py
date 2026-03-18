from app import errors
from app.cafe import Cafe


def go_to_cafe(cafe: Cafe, friends: list) -> str:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except errors.VaccineError:
            return "All friends should be vaccinated"
        except errors.NotWearingMaskError:
            if friend["wearing_a_mask"] is False:
                masks_to_buy += 1
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
