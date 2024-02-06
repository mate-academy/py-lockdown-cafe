from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends, cafe):
    counter = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            counter += 1
    if counter > 0:
        return f"Friends should buy {counter} masks"

    return f"Friends can go to {cafe.name}"
