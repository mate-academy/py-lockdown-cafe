import datetime
from typing import List, Dict, Any
from app.cafe import Cafe


def go_to_cafe(friends: List[Dict[str, Any]], cafe: Cafe) -> str:
    """
    :param friends: A list of friends,
     each represented by a dictionary with their details.
    :param cafe: An instance of the Cafe class
     representing the cafe being visited.
    :return: A message about the visit to the cafe.
    """
    if any("vaccine" not in friend for friend in friends):
        return "All friends should be vaccinated"
    not_vaccinated_count = sum(
        1 for friend in friends
        if friend["vaccine"]["expiration_date"] < datetime.date.today()
    )

    mask_needed_count = sum(
        1 for friend in friends
        if not friend.get("wearing_a_mask", True)
    )

    if not_vaccinated_count > 0:
        return "All friends should be vaccinated"

    if mask_needed_count > 0:
        return (f"Friends should buy {mask_needed_count} "
                f"mask{"s" if mask_needed_count > 1 else ""}")

    return f"Friends can go to {cafe.name}"
