from typing import List, Dict
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: List[Dict], cafe: Cafe) -> str:
    """
    Determine if a group of friends can visit a cafe based on vaccination
    and mask-wearing status.

    Args:
        friends (List[Dict]): A list of dictionaries containing information
                              about each friend.
        cafe (Cafe): The cafe to visit.

    Returns:
        str: A message indicating whether the friends can visit the cafe or
             what they need to do to comply.
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
