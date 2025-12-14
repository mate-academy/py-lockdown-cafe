from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        try:
            print(cafe.visit_cafe(friend))
        except VaccineError as v:
            print(v)
            return "All friends should be vaccinated"
        except NotWearingMaskError as n:
            print(n)
            masks_to_buy += 1

    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
