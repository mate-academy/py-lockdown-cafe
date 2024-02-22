from datetime import date
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_needed = 0
    for friend in friends:
        if ("vaccine" not in friend
                or friend["vaccine"]["expiration_date"] < date.today()):
            return "All friends should be vaccinated"
        if not friend.get("wearing_a_mask", False):
            masks_needed += 1
    if masks_needed > 0:
        return f"Friends should buy {masks_needed} masks"
    return f"Friends can go to {cafe.name}"
