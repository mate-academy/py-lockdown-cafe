from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    count_masks = 0
    all_vaccinated = True
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            all_vaccinated = False
        except NotWearingMaskError:
            count_masks += 1

    if not all_vaccinated:
        return ("All friends should be vaccinated")
    elif count_masks > 0:
        return (f"Friends should buy {count_masks} masks")
    else:
        return f"Friends can go to {cafe.name}"
