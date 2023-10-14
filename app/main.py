from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    need_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError as e:
            return f"{e}"
        except NotWearingMaskError:
            need_mask += 1
    if need_mask == 0:
        return f"Friends can go to {cafe.name}"
    else:
        return f"Friends should buy {need_mask} masks"
