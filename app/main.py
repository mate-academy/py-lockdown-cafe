from app.cafe import (Cafe,
                      NotWearingMaskError)
from app.errors import VaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str | None:
    counter = 0
    for dict_friends in friends:
        try:
            cafe.visit_cafe(dict_friends)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            counter += 1
    if counter > 0:
        return f"Friends should buy {counter} masks"
    return f"Friends can go to {cafe.name}"
