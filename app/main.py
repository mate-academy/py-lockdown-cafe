from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    """Check if all friends can visit the cafe and return appropriate
    message.

    Args:
        friends: List of friend dictionaries with visitor information.
        cafe: The cafe instance to visit.

    Returns:
        "Friends can go to {cafe.name}" if all friends can visit.
        "All friends should be vaccinated" if any friend has vaccine
        issues.
        "Friends should buy {count} masks" if all vaccinated but some
        not wearing masks.
    """
    vaccine_issues = 0
    mask_issues = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccine_issues += 1
        except NotWearingMaskError:
            mask_issues += 1

    if vaccine_issues:
        return "All friends should be vaccinated"
    elif mask_issues:
        return f"Friends should buy {mask_issues} masks"

    return f"Friends can go to {cafe.name}"
