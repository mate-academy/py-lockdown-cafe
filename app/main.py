from .cafe import Cafe
from .errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    mask_count = 0
    try:
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except NotWearingMaskError:
                mask_count += 1
        return (f"Friends can go to {cafe.name}" if not mask_count
                else f"Friends should buy {mask_count} masks")
    except VaccineError:
        return "All friends should be vaccinated"
