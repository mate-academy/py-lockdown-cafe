import datetime
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    mask_missing_count = 0

    for friend in friends:
        if (
                "vaccine" not in friend
                or friend["vaccine"].get("expiration_date")
                < datetime.date.today()
        ):
            return "All friends should be vaccinated"

        wearing_a_mask = friend.get("wearing_a_mask", False)
        if not wearing_a_mask:
            mask_missing_count += 1

    if mask_missing_count > 0:
        return f"Friends should buy {mask_missing_count} masks"

    return f"Friends can go to {cafe.name}"
