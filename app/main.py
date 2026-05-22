from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    friends_can_go_to_cafe = 0
    count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            friends_can_go_to_cafe += 1
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count += 1
    if count > 0:
        return f"Friends should buy {count} masks"
    return f"Friends can go to {cafe.name}"
