from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: str) -> str:
    v, m = 0, 0
    for friend in friends:
        mate = Cafe(cafe)
        try:
            mate.visit_cafe(friend)
        except VaccineError:
            v += 1
        except NotWearingMaskError:
            m += 1
    if v > 0:
        return "All friends should be vaccinated"
    if m > 0:
        return f"Friends should buy {m} masks"
    return f"Friends can go to {cafe.name}"
