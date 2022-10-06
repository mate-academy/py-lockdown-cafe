from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe):
    count_mask = 0
    count_friends = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            count_friends += 1
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_mask += 1
    if count_mask > 0:
        return f"Friends should buy {count_mask} masks"
    if count_friends == len(friends):
        return f"Friends can go to {cafe.name}"
