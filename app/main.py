from app.errors import (
    NotWearingMaskError,
    VaccineError
)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe):
    everyone_has_vac = True
    persons_without_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            everyone_has_vac = False
        except NotWearingMaskError:
            persons_without_mask += 1
    if everyone_has_vac is False:
        return "All friends should be vaccinated"
    if persons_without_mask > 0:
        return f"Friends should buy {persons_without_mask} masks"
    return f"Friends can go to {cafe.name}"
