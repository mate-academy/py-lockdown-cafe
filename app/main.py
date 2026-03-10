from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: str) -> str:
    masks_to_buy = 0
    all_vaccinated = True
    for friend in friends:
        try:
            Cafe(cafe).visit_cafe(friend)
        except VaccineError:
            all_vaccinated = False
        except NotWearingMaskError:
            masks_to_buy += 1
    if all_vaccinated is False:
        return "All friends should be vaccinated"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
