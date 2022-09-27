from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: object):
    friends_counter = counter = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            friends_counter += 1
        except VaccineError as va:
            return va.args[0]
        except NotWearingMaskError:
            counter += 1
    if counter != 0:
        return f"Friends should buy {counter} masks"
    elif friends_counter == len(friends):
        return f"Friends can go to {cafe.name}"
