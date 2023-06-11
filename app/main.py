from app.cafe import Cafe

from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe: "Cafe") -> str:
    masks_counter = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_counter += 1

    if not masks_counter:
        return f"Friends can go to {cafe.name}"
    return f"Friends should buy {masks_counter} masks"
