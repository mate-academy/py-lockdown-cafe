from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    """
    Determines if a group of friends can visit the cafe.

    - If at least one friend is unvaccinated,
     return: "All friends should be vaccinated."
    - If all are vaccinated but some aren't wearing masks,
     return: "Friends should buy {masks_to_buy} masks."
    - If everyone meets the requirements,
     return: "Friends can go to {cafe.name}."
    """
    masks_needed = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_needed += 1

    if masks_needed > 0:
        return f"Friends should buy {masks_needed} masks"

    return f"Friends can go to {cafe.name}"
