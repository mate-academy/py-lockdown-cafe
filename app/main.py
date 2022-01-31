from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe):
    masks_to_buy = 0
    for one in friends:
        if not one["wearing_a_mask"]:
            masks_to_buy += 1

    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
