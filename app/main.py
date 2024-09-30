from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    count_not_wear_mask = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_not_wear_mask += 1

    if count_not_wear_mask > 0:
        return f"Friends should buy {count_not_wear_mask} masks"
    return f"Friends can go to {cafe.name}"
