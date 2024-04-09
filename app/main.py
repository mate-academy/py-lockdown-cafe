from app.cafe import Cafe
import app.errors as err


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    mask_err_count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except err.VaccineError:
            return "All friends should be vaccinated"
        except err.NotWearingMaskError:
            mask_err_count += 1
    if mask_err_count:
        return f"Friends should buy {mask_err_count} masks"

    return f"Friends can go to {cafe.name}"
