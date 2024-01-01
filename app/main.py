from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    not_vaccinated = []
    not_wearing_mask = []
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            not_vaccinated.append(friend)
        except NotWearingMaskError:
            not_wearing_mask.append(friend)
    if not_vaccinated:
        return "All friends should be vaccinated"
    if not_wearing_mask:
        return f"Friends should buy {len(not_wearing_mask)} masks"
    return f"Friends can go to {cafe.name}"
