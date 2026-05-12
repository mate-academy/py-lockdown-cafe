from app.cafe import Cafe

from app.errors import (VaccineError, NotWearingMaskError)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    unvaccinated_friends_exist = False
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            unvaccinated_friends_exist = True
        except NotWearingMaskError:
            masks_to_buy += 1

    if unvaccinated_friends_exist:
        return "All friends should be vaccinated"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
