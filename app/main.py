from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    try:
        masks_to_buy = 0
        for person_info in friends:
            try:
                cafe.visit_cafe(person_info)
            except NotWearingMaskError:
                masks_to_buy += 1
    except VaccineError:
        return "All friends should be vaccinated"
    return (f"Friends can go to {cafe.name}"
            if not masks_to_buy
            else f"Friends should buy {masks_to_buy} masks")
