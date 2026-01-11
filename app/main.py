from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError,
)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    problems = {"mask": 0}

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            problems["mask"] += 1

    if problems["mask"] > 0:
        return f"Friends should buy {problems['mask']} masks"

    return f"Friends can go to {cafe.name}"
