from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def count_masks(visitors: list) -> int:
    return sum(1 for person in visitors
               if not person.get("wearing_a_mask", False))


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    not_wearing_mask = False

    try:
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except NotWearingMaskError:
                not_wearing_mask = True
            except VaccineError:
                raise  # піднімаємо одразу, бо це пріоритет
    except VaccineError:
        return "All friends should be vaccinated"

    if not_wearing_mask:
        return f"Friends should buy {count_masks(friends)} masks"

    return f"Friends can go to {cafe.name}"
