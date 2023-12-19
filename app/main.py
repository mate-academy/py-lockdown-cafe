from __future__ import annotations
from app.cafe import Cafe
from app.errors import (VaccineError, NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    try:
        sorted_friends = sorted(friends,
                                key=lambda x: x["vaccine"]["expiration_date"])

        for friend in sorted_friends:
            cafe.visit_cafe(friend)
    except KeyError:
        return "All friends should be vaccinated"
    except VaccineError:
        return "All friends should be vaccinated"
    except NotWearingMaskError:
        masks_to_buy = len([friend["wearing_a_mask"]
                            for friend in sorted_friends
                            if not friend["wearing_a_mask"]])
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
