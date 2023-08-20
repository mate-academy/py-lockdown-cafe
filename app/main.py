import app.errors as errors
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: str) -> str:
    Cafe(cafe)
    validate_by_vaccine = []
    validate_by_mask = []

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except errors.VaccineError:
            validate_by_vaccine.append(False)
        except errors.NotWearingMaskError:
            validate_by_mask.append(False)

    if False not in validate_by_vaccine and False not in validate_by_mask:
        return f"Friends can go to {cafe.name}"
    elif False in validate_by_vaccine:
        return "All friends should be vaccinated"
    elif False in validate_by_mask:
        return f"Friends should buy {validate_by_mask.count(False)} masks"
