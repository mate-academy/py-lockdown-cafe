import datetime
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    num_maskless = 0
    for friend in friends:
        if "vaccine" not in friend:
            return "All friends should be vaccinated"

        expiration_date = friend["vaccine"].get("expiration_date")
        if expiration_date < datetime.date.today():
            return "All friends should be vaccinated"

        if not friend.get("wearing_a_mask", False):
            num_maskless += 1

    return (f"Friends should buy {num_maskless} "
            f"mask{"s" if num_maskless > 1 else ""}") if num_maskless > 0 \
        else f"Friends can go to {cafe.name}"
