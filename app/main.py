from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    friends_without_vaccine = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            friends_without_vaccine += 1
        except NotWearingMaskError:
            masks_to_buy += 1

    if friends_without_vaccine > 0:
        return "All friends should be vaccinated"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
