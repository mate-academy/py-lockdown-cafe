from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends, cafe):
    masks_to_buy = 0
    try:
        for visitor in friends:
            try:
                cafe.visit_cafe(visitor)
            except NotWearingMaskError:
                masks_to_buy += 1
        if masks_to_buy == 0:
            return f"Friends can go to {cafe.name}"
    except VaccineError:
        return "All friends should be vaccinated"
    else:
        return f"Friends should buy {masks_to_buy} masks"
