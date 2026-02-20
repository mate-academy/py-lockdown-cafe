from app.cafe import Cafe
import datetime


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    for friend in friends:
        if "vaccine" not in friend:
            return "All friends should be vaccinated"
        if friend["vaccine"]["expiration_date"] < datetime.date.today():
            return "All friends should be vaccinated"
    masks_needed = sum(1 for friend in friends
                       if not friend.get("wearing_a_mask", False))
    if masks_needed > 0:
        return f"Friends should buy {masks_needed} masks"

    return f"Friends can go to {cafe.name}"
