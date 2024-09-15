from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends, cafe):
    vaccines = 0
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccines += 1
        except NotWearingMaskError:
            masks_to_buy += 1
    if vaccines != 0:
        return "All friends should be vaccinated"
    if masks_to_buy != 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
