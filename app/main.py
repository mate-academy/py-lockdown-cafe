from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe):
    friends_without_masks = 0
    friends_without_vaccine = 0

    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            friends_without_vaccine += 1
        except NotWearingMaskError:
            friends_without_masks += 1

    if friends_without_vaccine:
        return "All friends should be vaccinated"
    elif friends_without_masks:
        return f"Friends should buy {friends_without_masks} masks"
    return f"Friends can go to {cafe.name}"
