from app.cafe import Cafe
from app.errors import VaccineError
from app.errors import NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    errors = 0
    for person in friends:
        try:
            Cafe.visit_cafe(cafe, person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            errors += 1
    if errors > 0:
        return f"Friends should buy {errors} masks"
    return f"Friends can go to {cafe.name}"
