import datetime
from .cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    vaccine_issues = 0
    masks_to_buy = 0
    for friend in friends:
        if not friend["wearing_a_mask"]:
            masks_to_buy += 1
        if "vaccine" in friend:
            friend_vaccine = friend["vaccine"]
            if friend_vaccine["expiration_date"] < datetime.date.today():
                vaccine_issues += 1
                return "All friends should be vaccinated"
        if "vaccine" not in friend:
            vaccine_issues += 1
            return "All friends should be vaccinated"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    if masks_to_buy == 0 and vaccine_issues == 0:
        return f"Friends can go to {cafe.name}"
