from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    count_errors = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_errors += 1
    if count_errors != 0:
        return f"Friends should buy {count_errors} masks"

    if count_errors == 0:
        return f"Friends can go to {cafe.name}"
