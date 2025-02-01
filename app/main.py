from app.cafe import Cafe
from app.errors import (VaccineError,
                        NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccinated_count = 0
    with_mask_count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            vaccinated_count += 1
        except VaccineError:
            return "All friends should be vaccinated"
    if vaccinated_count == with_mask_count:
        return f"Friends can go to {cafe.name}"
    return f"Friends should buy {vaccinated_count - with_mask_count} masks"
