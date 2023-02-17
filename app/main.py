from app.cafe import Cafe

from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    not_wearing_mask_count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            not_wearing_mask_count += 1

    if not_wearing_mask_count:
        return (f"Friends should buy "
                f"{not_wearing_mask_count} masks")

    return f"Friends can go to {cafe.name}"
