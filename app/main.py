from datetime import date
from .cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    """
    Функція, яка перевіряє, чи можуть друзі піти в кафе.
    """
    not_vaccinated = 0
    outdated_vaccine = 0
    not_wearing_mask = 0

    for friend in friends:
        if "vaccine" not in friend:
            not_vaccinated += 1
        elif friend["vaccine"]["expiration_date"] < date.today():
            outdated_vaccine += 1

        if not friend["wearing_a_mask"]:
            not_wearing_mask += 1

    if not_vaccinated > 0 or outdated_vaccine > 0:
        return "All friends should be vaccinated"
    elif not_wearing_mask > 0:
        return f"Friends should buy {not_wearing_mask} masks"
    else:
        return f"Friends can go to {cafe.name}"
