import datetime
from app.cafe import Cafe


def go_to_cafe(friends: dict, cafe: Cafe) -> str:
    vaccinated_friends = 0
    masks_to_buy = 0

    for friend in friends:
        if "vaccine" not in friend:
            return "All friends should be vaccinated"

        if (friend["vaccine"].get("expiration_date")
                and friend["vaccine"]["expiration_date"]
                < datetime.date.today()):
            return "All friends should be vaccinated"

        if not friend.get("wearing_a_mask"):
            masks_to_buy += 1
        else:
            vaccinated_friends += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
