from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    valid_results = []
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            valid_results.append(True)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            valid_results.append(False)

    if not all(valid_results):
        return f"Friends should buy {valid_results.count(False)} masks"
    return f"Friends can go to {cafe.name}"
