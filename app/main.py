from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count_mask = 0
    vaccine_problem = False
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            vaccine_problem = True

        except NotWearingMaskError:
            count_mask += 1
    if vaccine_problem is True:
        return "All friends should be vaccinated"
    elif count_mask != 0:
        return f"Friends should buy {count_mask} masks"
    else:
        return f"Friends can go to {cafe.name}"
