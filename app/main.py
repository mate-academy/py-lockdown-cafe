from app.cafe import Cafe
from app.errors import (VaccineError,
                        NotWearingMaskError)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    count_friends = 0
    without_mask = 0
    if friends:
        for friend in friends:
            try:
                Cafe.visit_cafe(cafe, friend)
                count_friends += 1
            except VaccineError:
                return "All friends should be vaccinated"
            except NotWearingMaskError:
                without_mask += 1
    if without_mask:
        return f"Friends should buy {without_mask} masks"
    if count_friends == len(friends):
        return f"Friends can go to {cafe.name}"
