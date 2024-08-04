from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    unvaccinated_friends_count = 0
    lacking_masks_count = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            lacking_masks_count += 1
        except VaccineError:
            unvaccinated_friends_count += 1

    if unvaccinated_friends_count != 0:
        return "All friends should be vaccinated"
    if lacking_masks_count != 0:
        return f"Friends should buy {lacking_masks_count} masks"

    return f"Friends can go to {cafe.name}"
