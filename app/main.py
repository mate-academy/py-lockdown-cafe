from app.errors import NotWearingMaskError
from app.errors import VaccineError


def go_to_cafe(friends: list, cafe: list[dict]) -> str:
    buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            buy += 1
        except VaccineError:
            return "All friends should be vaccinated"
    if buy:
        return f"Friends should buy {buy} masks"

    return f"Friends can go to {cafe.name}"
