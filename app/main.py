from datetime import date
from typing import List, Dict, Any
from app.cafe import Cafe


def go_to_cafe(friends: List[Dict[str, Any]], cafe: Cafe) -> str:
    """Checks if friends can go to the cafe."""

    # Перевірка вакцинації
    for friend in friends:
        vaccine = friend.get("vaccine")

        if vaccine is None:
            return "All friends should be vaccinated"

        if vaccine["expiration_date"] < date.today():
            return "All friends should be vaccinated"

    # Підрахунок масок
    no_mask_count = sum(
        1 for friend in friends if not friend.get("wearing_a_mask")
    )

    if no_mask_count == 0:
        return f"Friends can go to {cafe.name}"

    return f"Friends should buy {no_mask_count} masks"
