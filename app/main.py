from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    unvaccinated_count = 0
    unmasked_count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            unvaccinated_count += 1
        except NotWearingMaskError:
            unmasked_count += 1

    if unvaccinated_count:
        return "All friends should be vaccinated"
    if unmasked_count:
        return f"Friends should buy {unmasked_count} masks"
    return f"Friends can go to {cafe.name}"
