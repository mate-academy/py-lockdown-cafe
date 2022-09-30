from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    missing_masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            missing_masks += 1
    return (f"Friends should buy {missing_masks} masks" if missing_masks > 0
            else f"Friends can go to {cafe.name}")
