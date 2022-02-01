from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends, cafe):
    without_masks = sum(not friend["wearing_a_mask"] for friend in friends)
    try:
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except VaccineError:
                return "All friends should be vaccinated"
    except NotWearingMaskError:
        return f"Friends should buy {without_masks} masks"
    else:
        return f"Friends can go to {cafe.name}"
