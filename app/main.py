from typing import List
from app.errors import (
    VaccineError,
    NotWearingMaskError
)
from app.cafe import Cafe


def go_to_cafe(friends: List[dict], cafe: Cafe) -> str:
    count_not_wearing_mask = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except NotWearingMaskError:
            count_not_wearing_mask += 1
        except VaccineError as error_vaccine:
            return f"{error_vaccine}"
    if count_not_wearing_mask:
        return f"Friends should buy {count_not_wearing_mask} masks"
    return f"Friends can go to {cafe.name}"
