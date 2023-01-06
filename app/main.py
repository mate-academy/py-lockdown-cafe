from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    problems_with_vaccines = 0
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            problems_with_vaccines += 1
        except NotWearingMaskError:
            masks_to_buy += 1
    if problems_with_vaccines > 0:
        return "All friends should be vaccinated"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    if problems_with_vaccines == 0 and masks_to_buy == 0:
        return f"Friends can go to {cafe.name}"
