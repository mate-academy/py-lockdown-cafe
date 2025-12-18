from app.cafe import Cafe
from app.errors import (NotWearingMaskError, VaccineError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)

        except VaccineError:
            return "All friends should be vaccinated"

        except NotWearingMaskError:
            count += 1

    return f"Friends should buy {count} masks" if count\
        else f"Friends can go to {cafe.name}"
