from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccine_issue = False
    mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccine_issue = True
        except NotWearingMaskError:
            mask += 1

    if vaccine_issue:
        return "All friends should be vaccinated"

    if mask > 0:
        return f"Friends should buy {mask} masks"

    return f"Friends can go to {cafe.name}"
