from app.cafe import Cafe

from app.errors import VaccineError, NotWearingMaskError

def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    has_vaccine_problem = False
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            has_vaccine_problem = True
            break
        except NotWearingMaskError:
            masks_to_buy += 1
    if has_vaccine_problem is True:
        return "All friends should be vaccinated"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"




