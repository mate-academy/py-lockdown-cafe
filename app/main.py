from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccine_error = ""
    counter_friends_with_no_mask = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError as e:
            vaccine_error = e
        except NotWearingMaskError:
            counter_friends_with_no_mask += 1

    if vaccine_error:
        return str(vaccine_error)

    if counter_friends_with_no_mask > 0:
        return f"Friends should buy {counter_friends_with_no_mask} masks"

    return f"Friends can go to {cafe.name}"
