from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccine_error = 0
    mask_error = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccine_error += 1
        except NotWearingMaskError:
            mask_error += 1

    if vaccine_error + mask_error == 0:
        return f"Friends can go to {cafe.name}"
    if vaccine_error > 0:
        return "All friends should be vaccinated"
    if mask_error > 0:
        return f"Friends should buy {mask_error} masks"
