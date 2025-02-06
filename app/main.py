from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe: "Cafe") -> str:
    all_people = True
    need_masks_count = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            all_people = False
            return ("All friends should be vaccinated")
        except NotWearingMaskError:
            all_people = False
            need_masks_count += 1

    if all_people:
        return (f"Friends can go to {cafe.name}")
    if need_masks_count > 0:
        return (f"Friends should buy {need_masks_count} masks")
