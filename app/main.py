from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe):
    allowed_to_visit = 0
    masks_to_buy = 0
    cafe_class = Cafe(cafe)
    for friend in friends:
        try:
            Cafe.visit_cafe(cafe_class, friend)
            allowed_to_visit += 1
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
    if allowed_to_visit == len(friends):
        return f"Friends can go to {cafe.name}"
    else:
        return f"Friends should buy {masks_to_buy} masks"
