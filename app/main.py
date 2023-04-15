from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    count = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)

        except NotWearingMaskError:
            count += 1

        except VaccineError:
            return "All friends should be vaccinated"

    if count > 0:
        return f"Friends should buy {count} masks"

    return f"Friends can go to {cafe.name}"
