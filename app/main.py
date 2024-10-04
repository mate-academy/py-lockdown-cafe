from app.cafe import Cafe
from app.errors import VaccineError
from app.errors import NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    not_vaccinated = 0
    should_buy_mask = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except VaccineError:
            not_vaccinated += 1
        except NotWearingMaskError:
            should_buy_mask += 1
    if not_vaccinated != 0:
        return "All friends should be vaccinated"
    if should_buy_mask != 0:
        return f"Friends should buy {should_buy_mask} masks"
    if (not_vaccinated + should_buy_mask) == 0:
        return f"Friends can go to {cafe.name}"
