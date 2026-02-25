from app import errors
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except errors.VaccineError:
            return "All friends should be vaccinated"
        except errors.NotWearingMaskError:
            masks_count += 1

    if masks_count > 0:
        return f"Friends should buy {masks_count} masks"
    else:
        return f"Friends can go to {cafe.name}"
