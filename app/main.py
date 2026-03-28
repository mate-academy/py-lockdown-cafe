from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count = 0
    result = None
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            result = "All friends should be vaccinated"
        except NotWearingMaskError:
            count += 1

    if result:
        return result
    elif count:
        return f"Friends should buy {count} masks"
    return f"Friends can go to {cafe.name}"
