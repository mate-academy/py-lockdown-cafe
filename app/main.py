from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    unvaccinated = False
    without_a_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            unvaccinated = True
        except NotWearingMaskError:
            without_a_mask += 1
    if unvaccinated:
        return "All friends should be vaccinated"
    elif without_a_mask > 0:
        return f"Friends should buy {without_a_mask} masks"
    else:
        return f"Friends can go to {cafe.name}"
