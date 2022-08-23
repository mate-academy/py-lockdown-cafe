from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe):
    masks_to_buy = 0
    for friend in friends:
        if not friend["wearing_a_mask"]:
            masks_to_buy += 1
    try:
        if masks_to_buy >= 0 and cafe.visit_cafe(friend):
            for friend in friends:
                cafe.visit_cafe(friend)
        cafe.visit_cafe(friend)
    except VaccineError:
        return "All friends should be vaccinated"
    except NotWearingMaskError:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
