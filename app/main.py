from app.errors import (
    VaccineError,
    NotWearingMaskError
)
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    friend_num = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            friend_num += 1
    if friend_num:
        return f"Friends should buy {friend_num} masks"
    return f"Friends can go to {cafe.name}"
