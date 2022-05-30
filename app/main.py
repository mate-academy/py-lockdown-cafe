from app import errors


def go_to_cafe(friends: list, cafe):
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except errors.VaccineError:
            return "All friends should be vaccinated"
        except errors.NotWearingMaskError:
            masks_to_buy += 1

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except errors.NotWearingMaskError:
            return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
