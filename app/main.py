from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count_of_musks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (VaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_of_musks += 1

    if count_of_musks:
        return f"Friends should buy {count_of_musks} masks"
    return f"Friends can go to {cafe.name}"
