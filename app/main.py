from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    # Check each friend's eligibility to visit
    try:
        masks_needed = 0
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except NotWearingMaskError:
                masks_needed += 1

            except VaccineError:
                return "All friends should be vaccinated"

        if masks_needed:
            return f"Friends should buy {masks_needed} masks"

        return f"Friends can go to {cafe.name}"

    except Exception as e:
        return str(e)
