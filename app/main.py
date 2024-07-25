from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    problems_with_vaccines = 0
    missing_masks = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            problems_with_vaccines += 1
        except NotWearingMaskError:
            missing_masks += 1

    if problems_with_vaccines:
        return "All friends should be vaccinated"

    if missing_masks:
        return f"Friends should buy {missing_masks} masks"

    return "Friends can go to KFC"
