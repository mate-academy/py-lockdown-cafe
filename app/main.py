from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict[str, object]], cafe: Cafe) -> str:
    """Determines if a group of friends can visit the cafe.

    Args:
        friends (list[dict[str, object]]): List of visitors.
        cafe (Cafe): The cafe instance.

    Returns:
        str: A message indicating if friends can visit the cafe,
             if they need masks, or if they are not vaccinated.
    """
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
