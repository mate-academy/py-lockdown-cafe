from app.cafe import Cafe

from app.errors import (
    VaccineError,
    NotWearingMaskError,
)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    friends_without_mask = sum(
        1 for friend in friends if not friend["wearing_a_mask"]
    )

    vaccination_error_count = 0
    mask_error_count = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccination_error_count += 1
        except NotWearingMaskError:
            mask_error_count += 1

    if vaccination_error_count:
        return "All friends should be vaccinated"

    if mask_error_count:
        return f"Friends should buy {friends_without_mask} masks"

    return f"Friends can go to {cafe.name}"
