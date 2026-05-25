from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    vaccinated_ok = True
    mask_violations = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)

        except VaccineError:
            vaccinated_ok = False
            break

        except NotWearingMaskError:
            mask_violations += 1

    if not vaccinated_ok:
        return "All friends should be vaccinated"

    if mask_violations > 0:
        return f"Friends should buy {mask_violations} masks"

    return f"Friends can go to {cafe.name}"
