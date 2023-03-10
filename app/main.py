from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: object) -> str:
    count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count += 1
    if count > 0:
        return f"Friends should buy {count} masks"
    return f"Friends can go to {cafe.name}"
