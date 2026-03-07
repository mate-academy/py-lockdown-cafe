from app import cafe
from app import errors


def go_to_cafe(friends: list, cafe: cafe.Cafe) -> str:
    masks_needed = 0
    all_vacinated = True
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except errors.NotWearingMaskError:
            masks_needed += 1
        except errors.VaccineError:
            all_vacinated = False

    if not all_vacinated:
        return "All friends should be vaccinated"
    if masks_needed:
        return f"Friends should buy {masks_needed} masks"
    return f"Friends can go to {cafe.name}"
