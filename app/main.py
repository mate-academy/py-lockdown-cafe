from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: dict, cafe: Cafe) -> str:
    if isinstance(friends, dict):
        friends = [friends]

    not_vaccinated = 0
    not_wearing_mask = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            not_vaccinated += 1
        except NotWearingMaskError:
            not_wearing_mask += 1

    if not_vaccinated > 0:
        return "All friends should be vaccinated"
    elif not_wearing_mask > 0:
        return f"Friends should buy {not_wearing_mask} masks"

    return f"Friends can go to {cafe.name}"
