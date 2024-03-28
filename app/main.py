from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    count_of_non_vaccinated = 0
    do_not_have_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            count_of_non_vaccinated += 1
        except NotWearingMaskError:
            do_not_have_mask += 1

    if count_of_non_vaccinated:
        return "All friends should be vaccinated"
    if do_not_have_mask:
        return f"Friends should buy {do_not_have_mask} masks"
    return f"Friends can go to {cafe.name}"
