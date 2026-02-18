from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_needed = 0
    vaccination_issues = 0

    # Check all friends first
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except VaccineError:
            vaccination_issues += 1
        except NotWearingMaskError:
            masks_needed += 1

    # Return results based on what was found
    if vaccination_issues > 0:
        return "All friends should be vaccinated"
    if masks_needed > 0:
        return f"Friends should buy {masks_needed} masks"
    return f"Friends can go to {cafe.name}"

