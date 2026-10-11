from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    has_vaccine_issue = False
    masks = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            has_vaccine_issue = True
        except NotWearingMaskError:
            masks += 1
    if has_vaccine_issue:
        return "All friends should be vaccinated"
    if masks:
        return f"Friends should buy {masks} masks"
    else:
        return f"Friends can go to {cafe.name}"
