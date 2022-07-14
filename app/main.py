from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends, cafe):
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
    return (f"Friends can go to {cafe.name}"
            if not masks_to_buy
            else f"Friends should buy {masks_to_buy} masks")
