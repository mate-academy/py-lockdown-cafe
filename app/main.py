from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    vaccinated = True
    mask_needed_counter = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccinated = False
        except NotWearingMaskError:
            mask_needed_counter += 1
    if vaccinated is False:
        return "All friends should be vaccinated"
    if mask_needed_counter == 0 and vaccinated is True:
        return f"Friends can go to {cafe.name}"
    if mask_needed_counter > 0:
        return f"Friends should buy {mask_needed_counter} masks"
