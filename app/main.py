from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    errors = [0, 0]

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            errors[0] += 1
        except NotWearingMaskError:
            errors[1] += 1

    if errors[0] > 0:
        return "All friends should be vaccinated"
    elif errors[1] > 0:
        return f"Friends should buy {errors[1]} masks"
    return f"Friends can go to {cafe.name}"
