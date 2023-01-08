from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    not_wearing_mask = []
    counter = 0
    for friend in friends:
        counter += 1
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError as e:
            not_wearing_mask.append(e)
        if counter == len(friends) and len(not_wearing_mask) >= 1:
            return f"Friends should buy {len(not_wearing_mask)} masks"
    return f"Friends can go to {cafe.name}"
