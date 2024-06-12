from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count_of_non_vaccinated = 0
    count_of_musks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (VaccineError):
            count_of_non_vaccinated += 1
        except NotWearingMaskError:
            count_of_musks += 1

    if count_of_non_vaccinated:
        return "All friends should be vaccinated"
    elif count_of_musks:
        return f"Friends should buy {count_of_musks} masks"
    return f"Friends can go to {cafe.name}"
