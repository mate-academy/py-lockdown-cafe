from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    unvaccinated = 0
    no_mask = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            unvaccinated += 1
        except NotWearingMaskError:
            no_mask += 1

    if not unvaccinated and no_mask > 0:
        masks_to_buy = no_mask
        return f"Friends should buy {masks_to_buy} masks"
    elif unvaccinated:
        return "All friends should be vaccinated"
    return f"Friends can go to {cafe.name}"
