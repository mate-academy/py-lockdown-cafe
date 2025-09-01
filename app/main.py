from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    vaccine_error = 0
    mask_error = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccine_error += 1
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_error += 1

    masks_to_buy = mask_error

    if not (vaccine_error + mask_error):
        return f"Friends can go to {cafe.name}"
    if mask_error > 0:
        return f"Friends should buy {masks_to_buy} masks"
