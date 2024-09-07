from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError,
)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    """
    Determines if a group of friends can visit the cafe
    based on their health status.

    Args:
        friends (list[dict]):
            A list of dictionaries where each dictionary represents
            a friend with keys for 'vaccine' and 'wearing_a_mask'.
            cafe (Cafe): The Cafe instance they want to visit.

    Returns:
        str: A message indicating whether the friends can visit the cafe,
        whether they need to buy masks,
        or whether everyone should be vaccinated.
    """

    masks_to_buy = 0

    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
