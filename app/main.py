from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: object) -> str:
    count_of_mask = 0

    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_of_mask += 1

    if count_of_mask:
        return f"Friends should buy {count_of_mask} masks"
    else:
        return f"Friends can go to {cafe.name}"
