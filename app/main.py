from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:

    masks_to_buy = 0
    has_vaccine_error = False

    for friend in friends:
        try:
            cafe.visit_cafe(visitor=friend)

        except VaccineError:
            has_vaccine_error = True
            break

        except NotWearingMaskError:
            masks_to_buy += 1

    if not masks_to_buy and not has_vaccine_error:
        return f"Friends can go to {cafe.name}"

    if has_vaccine_error:
        return "All friends should be vaccinated"

    return f"Friends should buy {masks_to_buy} masks"
