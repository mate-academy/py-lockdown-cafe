from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    non_vaccine = 0
    masks_to_buy = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            non_vaccine += 1
        except NotWearingMaskError:
            masks_to_buy += 1
    if non_vaccine > 0:
        return "All friends should be vaccinated"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
