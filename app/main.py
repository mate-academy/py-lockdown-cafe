from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccinated_count = len(friends)
    mask_count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccinated_count -= 1
        except NotWearingMaskError:
            mask_count += 1
    if vaccinated_count != len(friends):
        return "All friends should be vaccinated"
    if mask_count != 0:
        return f"Friends should buy {mask_count} masks"
    else:
        return f"Friends can go to {cafe.name}"
