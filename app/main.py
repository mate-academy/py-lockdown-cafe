from app.cafe import Cafe

from app.errors import NotWearingMaskError
from app.errors import VaccineError


def go_to_cafe(friends: dict, cafe: Cafe) -> str | None:
    masks_to_buy = 0
    visitors = 0
    for friend in friends:
        try:
            Cafe.visit_cafe(cafe, friend)
            visitors += 1
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    if visitors == len(friends):
        return f"Friends can go to {cafe.name}"
