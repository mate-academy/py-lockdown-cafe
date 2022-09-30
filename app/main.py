from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: dict, cafe: Cafe) -> str:
    persons_without_mask = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            persons_without_mask += 1
    if persons_without_mask:
        return f"Friends should buy {persons_without_mask} masks"
    return f"Friends can go to {cafe.name}"
