from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: "Cafe") -> str:
    without_mask_count = 0
    count = 0
    for friend in friends:
        count += 1
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            without_mask_count += 1
            if count == len(friends):
                return f"Friends should buy {without_mask_count} masks"
    if without_mask_count != 0:
        return f"Friends should buy {without_mask_count} masks"
    return f"Friends can go to {cafe.name}"
