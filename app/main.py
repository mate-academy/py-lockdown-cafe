from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    number_of_mask = []
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            number_of_mask.append(False)
    if len(number_of_mask) > 0:
        return f"Friends should buy {len(number_of_mask)} masks"
    return f"Friends can go to {cafe.name}"
