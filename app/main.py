from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    errors = {
        "not_vaccinated": 0,
        "not_wearing_mask": 0
    }

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            errors["not_vaccinated"] += 1
        except NotWearingMaskError:
            errors["not_wearing_mask"] += 1

    if errors["not_vaccinated"]:
        return "All friends should be vaccinated"
    elif errors["not_wearing_mask"]:
        return f"Friends should buy {errors['not_wearing_mask']} masks"
    else:
        return f"Friends can go to {cafe.name}"
