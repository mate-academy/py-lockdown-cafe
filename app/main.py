from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks = 0

    for person in friends:
        try:
            cafe.visit_cafe(person)

        except NotWearingMaskError:
            masks += 1

        except VaccineError:
            return "All friends should be vaccinated"

    if masks > 0:
        return f"Friends should buy {masks} masks"

    else:
        return f"Friends can go to {cafe.name}"
