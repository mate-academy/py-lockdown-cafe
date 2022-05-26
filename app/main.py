from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends, cafe):
    masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"

        except NotWearingMaskError:
            masks += 1

    if masks:
        return f"Friends should buy {masks} masks"

    return f"Friends can go to {cafe.name}"
