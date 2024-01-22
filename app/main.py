from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    success = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            success += 1
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    elif len(friends) == success:
        return f"Friends can go to {cafe.name}"
