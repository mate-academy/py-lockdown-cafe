from app.cafe import Cafe
from app.errors import (VaccineError,
                        NotWearingMaskError)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    counter = 0

    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            counter += 1

    if counter:
        return f"Friends should buy {counter} masks"

    return f"Friends can go to {cafe.name}"
