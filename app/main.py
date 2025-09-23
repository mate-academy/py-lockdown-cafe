import datetime
from .cafe import Cafe
from .errors import VaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    # 1. sprawdzamy szczepienia
    for friend in friends:
        try:
            if (
                "vaccine" not in friend
                or friend["vaccine"]["expiration_date"] < datetime.date.today()
            ):
                raise VaccineError
        except VaccineError:
            return "All friends should be vaccinated"

    # 2. sprawdzamy maski
    masks_to_buy = sum(
        1 for f in friends if not f.get("wearing_a_mask", False)
    )

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    # 3. wszystko OK
    return (
        f"Friends can go to "
        f"{cafe.name}"
    )
