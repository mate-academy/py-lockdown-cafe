from app.errors import VaccineError
from app.errors import NotWearingMaskError


def go_to_cafe(friends, cafe):
    count = 0
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            count += 1
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    if count == len(friends):
        return f"Friends can go to {cafe.name}"
