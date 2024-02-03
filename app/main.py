from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: object) -> str:
    masks_to_buy = 0
    vaccine_issues = False

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            masks_to_buy += 1
        except VaccineError:
            vaccine_issues = True
            break

    if vaccine_issues:
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
