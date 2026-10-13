from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            # Порахуй друзів без масок
            masks_needed = sum(
                1 for f in friends if not f.get("wearing_a_mask", False)
            )
            return f"Friends should buy {masks_needed} masks"

    return f"Friends can go to {cafe.name}"
