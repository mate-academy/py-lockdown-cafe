from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    need_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            need_mask += 1
        except VaccineError:
            return "All friends should be vaccinated"
    return (
        f"Friends can go to {cafe.name}"
        if not need_mask else
        f"Friends should buy {need_mask} masks"
    )
