from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: str):
    selected_cafe = Cafe(cafe)
    some_arr = []
    masks_to_buy = 0
    for person in friends:
        try:
            selected_cafe.visit_cafe(person)
            some_arr.append(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    if some_arr == friends:
        return f"Friends can go to {selected_cafe.name}"
