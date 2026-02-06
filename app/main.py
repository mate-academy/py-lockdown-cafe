from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    friend_with_no_vaccine = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            friend_with_no_vaccine += 1
        except NotWearingMaskError:
            masks_to_buy += 1

    if friend_with_no_vaccine > 0:
        return "All friends should be vaccinated"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    if friend_with_no_vaccine == 0 and masks_to_buy == 0:
        return f"Friends can go to {cafe.name}"
