from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: object) -> str:
    masks = 0
    for i in friends:
        try:
            Cafe.visit_cafe(cafe, i)
        except NotWearingMaskError:
            masks += 1
        except VaccineError:
            return "All friends should be vaccinated"
    if masks:
        return f"Friends should buy {masks} masks"
    return f"Friends can go to {cafe.name}"
