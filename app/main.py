from datetime import datetime
from typing import List

from app.cafe import Cafe
from app.errors import VaccineError


def go_to_cafe(cafe: Cafe, friends: List[dict]) -> str:
    vaccinated_friends = sum(
        1 for friend in friends if ("vaccine" in friend and (
            friend["vaccine"]["expiration_date"] >= (
                datetime.date(datetime.now())
            )
        ))
    )

    mask_wearing_friends = sum(
        1 for friend in friends if friend["wearing_a_mask"] is True
    )

    try:
        if vaccinated_friends == len(friends):
            if mask_wearing_friends == len(friends):
                return f"Friends can go to {cafe.name}"
            else:
                masks_to_buy = len(friends) - mask_wearing_friends
                return f"Friends should buy {masks_to_buy} masks"
        else:
            raise VaccineError("All friends should be vaccinated")
    except VaccineError as e:
        return str(e)
