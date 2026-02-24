from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str | None:
    masks_to_buy = 0
    must_be_vaccinated = False

    for visitor in friends:

        try:
            cafe.visit_cafe(visitor)
        except VaccineError:
            must_be_vaccinated = True
        except NotWearingMaskError:
            masks_to_buy += 1

    if must_be_vaccinated:
        return "All friends should be vaccinated"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
