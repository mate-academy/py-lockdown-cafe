from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_count = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_count += 1

        if masks_count > 0 and friend is friends[-1]:
            return f"Friends should buy {masks_count} masks"

    return f"Friends can go to {cafe.name}"
