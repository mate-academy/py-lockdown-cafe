from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(cafe: Cafe, friends: list):
    count_masks = 0

    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_masks += 1

    if count_masks:
        return f"Friends should buy {count_masks} masks"

    return f"Friends can go to {cafe.name}"
