import datetime
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    for friend in friends:
        vaccine = friend.get("vaccine")
        if not vaccine:
            return "All friends should be vaccinated"
        expiration = vaccine.get("expiration_date")
        if datetime.date.today() > expiration:
            return "All friends should be vaccinated"

    masks_to_buy = sum(1 for f in friends if not f.get("wearing_a_mask"))
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
