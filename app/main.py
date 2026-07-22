from app.cafe import Cafe
from app.errors import VaccineError
from datetime import date


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    try:
        for friend in friends:
            if "vaccine" not in friend:
                raise VaccineError("Відсутня вакцинація.")

            expiration_date = friend["vaccine"].get("expiration_date")
            if expiration_date < date.today():
                raise VaccineError("Вакцина прострочена.")

            if not friend.get("wearing_a_mask", False):
                masks_to_buy += 1
    except VaccineError:
        return "All friends should be vaccinated"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
