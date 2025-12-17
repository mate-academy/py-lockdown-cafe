from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    not_vaccinated_count = 0
    no_mask_count = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            not_vaccinated_count += 1
        except NotWearingMaskError:
            no_mask_count += 1

    if not_vaccinated_count > 0:
        return "All friends should be vaccinated"
    if no_mask_count > 0:
        return f"Friends should buy {no_mask_count} masks"
    return f"Friends can go to {cafe.name}"
