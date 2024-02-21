from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    all_vaccinated = True
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            all_vaccinated = False
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if all_vaccinated:
        if masks_to_buy == 0:
            return f"Friends can go to {cafe.name}"
        return f"Friends should buy {masks_to_buy} masks"
