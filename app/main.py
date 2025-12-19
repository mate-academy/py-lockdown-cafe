from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    not_vaccinated_count = 0
    not_wearing_mask_count = 0

    has_vaccine_issue = False

    for friend in friends:
        try:
            cafe.visit_cafe(friend)

        except VaccineError:
            not_vaccinated_count += 1
            has_vaccine_issue = True

        except NotWearingMaskError:
            not_wearing_mask_count += 1

    if has_vaccine_issue:
        return "All friends should be vaccinated"

    elif not_wearing_mask_count:
        return f"Friends should buy {not_wearing_mask_count} masks"

    else:
        return f"Friends can go to {cafe.name}"
