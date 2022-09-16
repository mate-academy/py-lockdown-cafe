from app.errors import VaccineError
from app.errors import NotWearingMaskError


def go_to_cafe(friends: list, cafe: object):
    mask = 0
    for i in friends:
        try:
            cafe.visit_cafe(i)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask += 1
    if mask > 0:
        return f"Friends should buy {mask} masks"
    return f"Friends can go to {cafe.name}"
