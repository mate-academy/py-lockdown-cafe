from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    buy_masks = 0
    not_vaccinated = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            buy_masks += 1
        except VaccineError:
            not_vaccinated += 1

    if not_vaccinated > 0:
        return "All friends should be vaccinated"

    if buy_masks > 0:
        return f"Friends should buy {buy_masks} masks"

    return f"Friends can go to {cafe.name}"
