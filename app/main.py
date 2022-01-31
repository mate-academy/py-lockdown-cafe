from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends, cafe):
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy = len([friend for friend in friends
                                if not friend["wearing_a_mask"]])
            return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
