from __future__ import annotations
import datetime
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    vaccinated_friends = (
        [friend for friend in friends if
         "vaccine" in friend and friend["vaccine"]["expiration_date"]
         >= datetime.date.today()]
    )
    non_masked_friends = (
        [friend for friend in vaccinated_friends
         if not friend["wearing_a_mask"]]
    )

    if len(vaccinated_friends) != len(friends):
        return "All friends should be vaccinated"
    elif non_masked_friends:
        return f"Friends should buy {len(non_masked_friends)} masks"
    else:
        return f"Friends can go to {cafe.name}"
